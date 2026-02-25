#!/usr/bin/env python3
"""
MMT TCS Reconciliation — Report Selection Analysis
====================================================
Determines which MMT extranet report is the correct basis for GSTR-8
reconciliation and produces the final reconciliation.

Data Sources (both from MMT Extranet):
  • Booking Reports  — filtered by MMT on BOOKING DATE ("Booked On")
  • Earnings Reports — filtered by MMT on CHECK-IN DATE ("Checkin Date")

GST Portal: GSTR-8 by MMT for Jan-2026 (27AADCM5146R1C6)
  Gross: ₹27,76,912 | Returns: ₹1,41,960 | Net: ₹26,34,952
  CGST TCS: ₹6,587.38 | SGST TCS: ₹6,587.38 | Total: ₹13,174.76
"""

import csv, glob
from pathlib import Path
from collections import defaultdict

BASE_DIR      = Path.cwd()
EARNINGS_DIR  = BASE_DIR / "EarningsReport"
BOOKINGS_DIR  = BASE_DIR / "BookingReports"

# ── Portal Constants ──────────────────────────────────────────────────────────
PORTAL_GROSS    = 2_776_912.00
PORTAL_RETURNS  =   141_960.00
PORTAL_NET      = 2_634_952.00
PORTAL_CGST_TCS =     6_587.38
PORTAL_SGST_TCS =     6_587.38
PORTAL_TOTAL_TCS = 13_174.76

YEAR, MONTH     = 2026, 1   # January 2026
MMT_BRANDS      = {"makemytrip", "goibibo", "mmtgcc", "mmt"}


# ── Utilities ─────────────────────────────────────────────────────────────────
def pf(v):
    try: return float(str(v).strip().replace(",", ""))
    except: return 0.0

def in_period(date_str, year=YEAR, month=MONTH):
    try:
        y, m, _ = str(date_str).strip()[:10].split("-")
        return int(y) == year and int(m) == month
    except: return False

def strip_tab(v): return str(v).strip().lstrip("\t").strip()

def load_csv_dir(directory, skip_zone=True):
    rows = []
    for f in sorted(glob.glob(str(Path(directory) / "*.csv"))):
        if skip_zone and ":Zone.Identifier" in f: continue
        with open(f, newline="", encoding="utf-8-sig") as fp:
            for r in csv.DictReader(fp):
                r["_file"] = Path(f).name
                rows.append(r)
    return rows


# ── Section 1: Legal Framework for Date Basis ───────────────────────────────
def print_legal_framework():
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║   REPORT SELECTION ANALYSIS — Which Report to Use for GSTR-8?      ║
╚══════════════════════════════════════════════════════════════════════╝

LEGAL FRAMEWORK — Section 52, CGST Act:
  "Every electronic commerce operator...shall...collect an amount...
   calculated at...the net value of taxable supplies...made through it..."
  
  KEY PHRASE: "Supplies MADE through it" during the tax period.

  ▶ A hotel accommodation SUPPLY is MADE when the customer completes
    the stay (i.e., at CHECK-OUT / over the check-in period).
  ▶ BOOKING DATE is when the contract is formed, NOT when supply is made.
  ▶ GST law mandates: TCS period = when supply is MADE (check-in month).

MMT EXTRANET REPORT DEFINITIONS:
  • Booking Reports  → Filtered by BOOKING DATE («Booked On» column)
  • Earnings Reports → Filtered by CHECK-IN DATE («Checkin Date» column)
  
  The Earnings Report aligns with the legal definition of supply period.
  
  HOWEVER — MMT files GSTR-8 based on its own internal accounting.
  In practice, many ECOs file on SETTLEMENT/PAYMENT basis. We must
  check which report ACTUALLY matches the GSTR-8 portal data to
  determine what MMT is using.
""")


# ── Section 2: Compute all three scenarios ───────────────────────────────────
def compute_all_scenarios(er_rows, br_rows):
    """
    Three ways to compute gross / TCS from MMT extranet:
      A. Earnings Reports filtered by CHECK-IN DATE (what user says ER uses)
      B. Booking Reports filtered by BOOKING DATE (what user says BR uses)
      C. Earnings Reports filtered by BOOKING DATE (cross-check)
    """
    results = {}

    # ── A: Earnings Report, CHECK-IN date in Jan-2026 ─────────────────────
    mmt_er_checkin = [
        r for r in er_rows
        if r.get("Brand", "").strip().lower() in MMT_BRANDS
        and in_period(r.get("Checkin Date", ""))
    ]
    er_conf = [r for r in mmt_er_checkin if r.get("Booking Status","").strip().lower()=="confirmed"]
    er_canc = [r for r in mmt_er_checkin if r.get("Booking Status","").strip().lower()=="cancelled"]
    results["A"] = {
        "label"        : "Earnings Report — CHECK-IN date = Jan-2026",
        "confirmed"    : len(er_conf),
        "cancelled"    : len(er_canc),
        "gross_conf"   : sum(pf(r.get("Property Gross Charges",0)) for r in er_conf),
        "gross_canc"   : sum(pf(r.get("Property Gross Charges",0)) for r in er_canc),
        "tcs_conf"     : sum(pf(r.get("TCS Amount",0)) for r in er_conf),
        "tcs_canc"     : sum(pf(r.get("TCS Amount",0)) for r in er_canc),
        "date_col"     : "Checkin Date",
        "source"       : "EarningsReport",
    }

    # ── B: Booking Report, BOOKING DATE ("Booked On") in Jan-2026 ─────────
    mmt_br_booking = [
        r for r in br_rows
        if r.get("Booking Vendor","").strip().lower() in MMT_BRANDS
        and in_period(r.get("Booked On",""))
    ]
    br_conf = [r for r in mmt_br_booking if r.get("Booking Status","").strip().lower()=="confirmed"]
    br_canc = [r for r in mmt_br_booking if r.get("Booking Status","").strip().lower()=="cancelled"]
    results["B"] = {
        "label"        : "Booking Report — BOOKING DATE = Jan-2026",
        "confirmed"    : len(br_conf),
        "cancelled"    : len(br_canc),
        "gross_conf"   : sum(pf(r.get("Hotel Gross Charges (A+B+C+T)",0)) for r in br_conf),
        "gross_canc"   : sum(pf(r.get("Hotel Gross Charges (A+B+C+T)",0)) for r in br_canc),
        "tcs_conf"     : sum(pf(r.get("TCS Amount",0)) for r in br_conf),
        "tcs_canc"     : sum(pf(r.get("TCS Amount",0)) for r in br_canc),
        "date_col"     : "Booked On",
        "source"       : "BookingReports",
    }

    # ── C: Earnings Report, BOOKING DATE in Jan-2026 (cross-check) ────────
    mmt_er_booking = [
        r for r in er_rows
        if r.get("Brand", "").strip().lower() in MMT_BRANDS
        and in_period(r.get("Booking Date", ""))
    ]
    erc_conf = [r for r in mmt_er_booking if r.get("Booking Status","").strip().lower()=="confirmed"]
    erc_canc = [r for r in mmt_er_booking if r.get("Booking Status","").strip().lower()=="cancelled"]
    results["C"] = {
        "label"        : "Earnings Report — BOOKING DATE = Jan-2026",
        "confirmed"    : len(erc_conf),
        "cancelled"    : len(erc_canc),
        "gross_conf"   : sum(pf(r.get("Property Gross Charges",0)) for r in erc_conf),
        "gross_canc"   : sum(pf(r.get("Property Gross Charges",0)) for r in erc_canc),
        "tcs_conf"     : sum(pf(r.get("TCS Amount",0)) for r in erc_conf),
        "tcs_canc"     : sum(pf(r.get("TCS Amount",0)) for r in erc_canc),
        "date_col"     : "Booking Date",
        "source"       : "EarningsReport",
    }

    # Compute derived fields
    for k, v in results.items():
        v["net_gross"] = v["gross_conf"] - v["gross_canc"]
        v["net_tcs"]   = v["tcs_conf"] - v["tcs_canc"]
        v["diff_gross"]   = v["net_gross"] - PORTAL_NET
        v["diff_tcs"]     = v["net_tcs"] - PORTAL_TOTAL_TCS
        v["diff_gross_vs_portal_gross"] = v["gross_conf"] - PORTAL_GROSS

    return results


# ── Section 3: Print comparison table ────────────────────────────────────────
def print_comparison(results):
    print("═"*70)
    print("SCENARIO COMPARISON — Which Report Matches the GSTR-8?")
    print("═"*70)
    print(f"\n{'Metric':<42} {'A':>10} {'B':>10} {'C':>10} {'Portal':>10}")
    print(f"{'-'*42} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")
    
    def row(label, key, fmt="{:>10,.0f}"):
        vals = [fmt.format(results[k][key]) for k in ["A","B","C"]]
        return f"  {label:<40} {vals[0]:>10} {vals[1]:>10} {vals[2]:>10}"

    print(row("Confirmed bookings (count)", "confirmed", "{:>10,}"))
    print(row("Cancelled bookings (count)", "cancelled", "{:>10,}"))
    print(f"  {'Gross — Confirmed (₹)':<40} {results['A']['gross_conf']:>10,.0f} {results['B']['gross_conf']:>10,.0f} {results['C']['gross_conf']:>10,.0f} {PORTAL_GROSS:>10,.0f}")
    print(f"  {'Gross — Cancelled / Returns (₹)':<40} {results['A']['gross_canc']:>10,.0f} {results['B']['gross_canc']:>10,.0f} {results['C']['gross_canc']:>10,.0f} {PORTAL_RETURNS:>10,.0f}")
    print(f"  {'NET Gross (₹)':<40} {results['A']['net_gross']:>10,.0f} {results['B']['net_gross']:>10,.0f} {results['C']['net_gross']:>10,.0f} {PORTAL_NET:>10,.0f}")
    print(f"  {'NET TCS (₹)':<40} {results['A']['net_tcs']:>10,.2f} {results['B']['net_tcs']:>10,.2f} {results['C']['net_tcs']:>10,.2f} {PORTAL_TOTAL_TCS:>10,.2f}")
    print(f"  {'── VARIANCES vs Portal ──':<40}")
    print(f"  {'Net Gross diff vs portal net (₹)':<40} {results['A']['diff_gross']:>+10,.0f} {results['B']['diff_gross']:>+10,.0f} {results['C']['diff_gross']:>+10,.0f}")
    print(f"  {'TCS diff vs portal TCS (₹)':<40} {results['A']['diff_tcs']:>+10,.2f} {results['B']['diff_tcs']:>+10,.2f} {results['C']['diff_tcs']:>+10,.2f}")

    print("\n  Scenario Definitions:")
    for k in ["A","B","C"]:
        print(f"    {k}: {results[k]['label']}")


# ── Section 4: Determine winning scenario ────────────────────────────────────
def determine_winner(results):
    print("\n" + "═"*70)
    print("VERDICT — Which Report to Use")
    print("═"*70)

    # Score by absolute difference from portal
    scores = {k: abs(results[k]["diff_gross"]) + abs(results[k]["diff_tcs"])*100
              for k in results}
    winner = min(scores, key=scores.get)

    for k in ["A","B","C"]:
        flag = "✅ BEST MATCH" if k == winner else ""
        print(f"\n  Scenario {k}: {results[k]['label']}")
        print(f"    Net Gross variance : ₹{results[k]['diff_gross']:>+12,.2f}")
        print(f"    TCS variance       : ₹{results[k]['diff_tcs']:>+12,.2f}")
        print(f"    Score (lower=better): {scores[k]:,.1f}  {flag}")

    res = results[winner]
    print(f"""
  ┌─────────────────────────────────────────────────────────────────┐
  │  CONCLUSION: Use  Scenario {winner}                                    │
  │  → {res['label']:<62}│
  │                                                                 │
  │  Reason: This report's figures are closest to MMT's GSTR-8     │
  │  filing for Jan-2026. MMT files GSTR-8 on this date basis.     │
  └─────────────────────────────────────────────────────────────────┘""")
    return winner


# ── Section 5: Full reconciliation with winning scenario ─────────────────────
def full_reconciliation(results, winner, er_rows, br_rows):
    res = results[winner]
    print("\n" + "═"*70)
    print(f"FINAL RECONCILIATION — {res['label']}")
    print("═"*70)

    # Re-derive rows for winner
    if winner == "A":
        mmt_rows = [r for r in er_rows
                    if r.get("Brand","").strip().lower() in MMT_BRANDS
                    and in_period(r.get("Checkin Date",""))]
        gross_col, tcs_col = "Property Gross Charges", "TCS Amount"
        brand_col, status_col = "Brand", "Booking Status"
        prop_col = lambda r: r["_file"].split("_net_earnings_")[0].title()
    elif winner == "B":
        mmt_rows = [r for r in br_rows
                    if r.get("Booking Vendor","").strip().lower() in MMT_BRANDS
                    and in_period(r.get("Booked On",""))]
        gross_col, tcs_col = "Hotel Gross Charges (A+B+C+T)", "TCS Amount"
        brand_col, status_col = "Booking Vendor", "Booking Status"
        prop_col = lambda r: r["_file"].replace("New_Bookings_Report_for_","").replace("_"," ").replace(".csv","")[:35]
    else:  # C
        mmt_rows = [r for r in er_rows
                    if r.get("Brand","").strip().lower() in MMT_BRANDS
                    and in_period(r.get("Booking Date",""))]
        gross_col, tcs_col = "Property Gross Charges", "TCS Amount"
        brand_col, status_col = "Brand", "Booking Status"
        prop_col = lambda r: r["_file"].split("_net_earnings_")[0].title()

    confirmed = [r for r in mmt_rows if r.get(status_col,"").strip().lower()=="confirmed"]
    cancelled = [r for r in mmt_rows if r.get(status_col,"").strip().lower()=="cancelled"]

    # ── Property-wise table ───────────────────────────────────────────────
    prop_data = defaultdict(lambda: {"count":0,"gross":0.0,"tcs":0.0})
    for r in confirmed:
        p = prop_col(r)
        prop_data[p]["count"] += 1
        prop_data[p]["gross"] += pf(r.get(gross_col,0))
        prop_data[p]["tcs"]   += pf(r.get(tcs_col,0))

    print(f"\n  Property-wise Breakdown (Confirmed bookings):")
    print(f"  {'Property':<38} {'Count':>7} {'Gross Charges':>16} {'TCS':>12}")
    print(f"  {'-'*38} {'-'*7} {'-'*16} {'-'*12}")
    t_count=t_gross=t_tcs=0
    for p in sorted(prop_data):
        d = prop_data[p]
        print(f"  {p:<38} {d['count']:>7} {d['gross']:>16,.2f} {d['tcs']:>12,.2f}")
        t_count+=d['count']; t_gross+=d['gross']; t_tcs+=d['tcs']
    print(f"  {'TOTAL Confirmed':<38} {t_count:>7} {t_gross:>16,.2f} {t_tcs:>12,.2f}")

    gross_conf = sum(pf(r.get(gross_col,0)) for r in confirmed)
    gross_canc = sum(pf(r.get(gross_col,0)) for r in cancelled)
    tcs_conf   = sum(pf(r.get(tcs_col,0))   for r in confirmed)
    tcs_canc   = sum(pf(r.get(tcs_col,0))   for r in cancelled)
    net_gross  = gross_conf - gross_canc
    net_tcs    = tcs_conf - tcs_canc

    # ── Reconciliation table ──────────────────────────────────────────────
    print(f"\n  ── Gross Value Reconciliation ──────────────────────────────")
    print(f"  {'Item':<48} {'Our Books (₹)':>14} {'Portal (₹)':>12}")
    print(f"  {'-'*48} {'-'*14} {'-'*12}")
    print(f"  {'Gross — Confirmed bookings':<48} {gross_conf:>14,.2f} {PORTAL_GROSS:>12,.2f}")
    print(f"  {'Gross — Cancelled / Returned':<48} {gross_canc:>14,.2f} {PORTAL_RETURNS:>12,.2f}")
    print(f"  {'NET Value':<48} {net_gross:>14,.2f} {PORTAL_NET:>12,.2f}")
    diff_gross = net_gross - PORTAL_NET
    print(f"  {'VARIANCE (Our Books − Portal)':<48} {diff_gross:>+14,.2f}")
    status_g = "✅ RECONCILED" if abs(diff_gross) < 5000 else f"⚠️  Diff ₹{diff_gross:,.0f}"
    print(f"  → {status_g}")

    print(f"\n  ── TCS Amount Reconciliation ────────────────────────────────")
    print(f"  {'Item':<48} {'Our Books (₹)':>14} {'Portal (₹)':>12}")
    print(f"  {'-'*48} {'-'*14} {'-'*12}")
    print(f"  {'TCS — Confirmed bookings':<48} {tcs_conf:>14,.2f} {PORTAL_CGST_TCS:>12,.2f}  (CGST)")
    print(f"  {'TCS — Cancelled / Returned':<48} {tcs_canc:>14,.2f} {PORTAL_SGST_TCS:>12,.2f}  (SGST)")
    print(f"  {'NET TCS (Books)':<48} {net_tcs:>14,.2f} {PORTAL_TOTAL_TCS:>12,.2f}  (Total)")
    diff_tcs = net_tcs - PORTAL_TOTAL_TCS
    print(f"  {'VARIANCE (Our Books − Portal)':<48} {diff_tcs:>+14,.2f}")
    status_t = "✅ RECONCILED" if abs(diff_tcs) < 500 else f"⚠️  Diff ₹{diff_tcs:,.2f}"
    print(f"  → {status_t}")

    if net_gross > 0:
        implied = (net_tcs / net_gross)*100
        print(f"\n  Implied TCS rate: {implied:.4f}%  |  Expected: 0.5000%  "
              f"({'✅ OK' if 0.45<=implied<=0.55 else '⚠️ CHECK'})")

    # ── Brand-wise breakdown ──────────────────────────────────────────────
    brand_data = defaultdict(lambda: {"count":0,"gross":0.0,"tcs":0.0})
    for r in confirmed:
        b = r.get(brand_col,"").strip()
        brand_data[b]["count"] += 1
        brand_data[b]["gross"] += pf(r.get(gross_col,0))
        brand_data[b]["tcs"]   += pf(r.get(tcs_col,0))

    print(f"\n  Brand-wise Breakdown:")
    print(f"  {'Brand':<20} {'Count':>7} {'Gross':>16} {'TCS':>12}")
    print(f"  {'-'*20} {'-'*7} {'-'*16} {'-'*12}")
    for b in sorted(brand_data):
        d = brand_data[b]
        print(f"  {b:<20} {d['count']:>7} {d['gross']:>16,.2f} {d['tcs']:>12,.2f}")

    return {"gross_conf":gross_conf,"gross_canc":gross_canc,"net_gross":net_gross,
            "tcs_conf":tcs_conf,"tcs_canc":tcs_canc,"net_tcs":net_tcs,
            "diff_gross":diff_gross,"diff_tcs":diff_tcs}


# ── Section 6: Residual variance investigation ───────────────────────────────
def investigate_residual(results, winner, er_rows):
    res = results[winner]
    if abs(res["diff_gross"]) < 1000:
        print("\n  ✅ Gross value variance is within ₹1,000 — no further investigation needed.")
        return

    print(f"\n  ── Residual Variance Analysis ({res['diff_gross']:+,.0f}) ───────────────")

    # Check if bookings in our data span outside Jan purely due to multi-night stays
    if winner in ("A","C"):
        date_field = "Checkin Date" if winner=="A" else "Booking Date"
        mmt_rows = [r for r in er_rows
                    if r.get("Brand","").strip().lower() in MMT_BRANDS
                    and in_period(r.get(date_field,""))]
    # Check checkout dates extending beyond Jan
    long_stay = [r for r in mmt_rows
                 if not in_period(r.get("Checkout Date",""))
                 and r.get("Booking Status","").strip().lower()=="confirmed"]
    cross_gross = sum(pf(r.get("Property Gross Charges",0)) for r in long_stay)
    if long_stay:
        print(f"  Bookings with checkout OUTSIDE Jan-2026: {len(long_stay)}")
        print(f"  Gross value of those bookings: ₹{cross_gross:,.2f}")
        print(f"  These may have been partially filed in Feb GSTR-8 by MMT.")


# ── Section 7: Action Plan ────────────────────────────────────────────────────
def action_plan(final: dict, winner: str):
    print("\n" + "═"*70)
    print("ACTION PLAN")
    print("═"*70)
    ok_tcs   = abs(final["diff_tcs"]) < 500
    ok_gross = abs(final["diff_gross"]) < 5000

    print(f"""
  STEP 1 — GSTR-8 PERIOD BASIS DETERMINATION
  ▶ MMT files GSTR-8 on {'BOOKING DATE' if winner=='B' else 'CHECK-IN DATE'} basis (Scenario {winner} matched best).
  ▶ Use {'Booking Reports (Booked On = month)' if winner=='B' else 'Earnings Reports (Checkin Date = month)'}
    as the standard reference for all future TCS reconciliations with MMT.

  STEP 2 — TCS CREDIT ACCEPTANCE
  {"  ✅ TCS Amount RECONCILED — ACCEPT the credit." if ok_tcs else f"  ⚠️  TCS variance ₹{final['diff_tcs']:+,.2f} — investigate before accepting."}
  
  On GST Portal:
    Services → Returns → TDS and TCS Credit Received → Jan-2026
    → ACCEPT the entry from 27AADCM5146R1C6 (MAKEMYTRIP INDIA PVT LTD)
    → File with DSC/EVC
    → TCS of ₹13,174.76 credited to Electronic Cash Ledger

  STEP 3 — ACCOUNTING ENTRY (after portal acceptance)
    Dr. Electronic Cash Ledger (GST)        ₹  6,587.38  [CGST]
    Dr. Electronic Cash Ledger (GST)        ₹  6,587.38  [SGST]
        Cr. TCS Receivable — MakeMyTrip     ₹ 13,174.76

  STEP 4 — GSTR-1 TABLE 14(a) REPORTING
    For Jan-2026 GSTR-1, report ECO supplies:
    ECO GSTIN    : 27AADCM5146R1C6
    Net Value    : ₹{PORTAL_NET:>12,.2f}  (use portal figure)
    [Informational — does NOT affect GSTR-3B liability]

  STEP 5 — GROSS VALUE VARIANCE (₹{final['diff_gross']:+,.0f})
  {"  ✅ Within acceptable tolerance — no action needed." if ok_gross else f"""  ⚠️  Variance exceeds tolerance. Likely causes:
    a) Bookings where check-in/booking straddle month boundaries
    b) Cancellations processed in a different period by MMT
    c) Manual adjustments not in the downloaded report period
    
    Actions:
    → Download the FULL January 2026 settlement statement from MMT
      (not filtered by date) and compare booking-by-booking.
    → Email compliance@makemytrip.com / your account manager
      requesting a GSTR-8 booking-level reconciliation for Jan-2026.
    → Cross-check with: Services → Returns → GSTR-2B for exact MMT data."""}

  STEP 6 — STANDARDISE GOING FORWARD
  ▶ Always use the {'BOOKING REPORT (filtered by booking date)' if winner=='B' else 'EARNINGS REPORT (filtered by check-in date)'}
    for monthly TCS reconciliation.
  ▶ Download by the 15th of each month (after MMT files GSTR-8 by 10th).
  ▶ File TCS credit acceptance before GSTR-3B due date.
""")


# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print_legal_framework()

    print("Loading data…")
    er_rows = load_csv_dir(EARNINGS_DIR)
    br_rows = load_csv_dir(BOOKINGS_DIR)
    print(f"  Earnings Report rows loaded: {len(er_rows)}")
    print(f"  Booking Report rows loaded : {len(br_rows)}")

    results = compute_all_scenarios(er_rows, br_rows)
    print_comparison(results)
    winner = determine_winner(results)
    final  = full_reconciliation(results, winner, er_rows, br_rows)
    investigate_residual(results, winner, er_rows)
    action_plan(final, winner)
