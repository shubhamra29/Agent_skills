---
name: gst-tcs-reconciliation
description: "This skill should be used when the user asks to reconcile GST TCS (Tax Collected at Source) from e-commerce operators (ECOs) like MakeMyTrip, Cleartrip, Airbnb, Yatra, Agoda, or TravelStack with their books of accounts. Covers GSTR-8 reconciliation, GSTR-2A TCS credit verification, accounting entries, GSTR-1 Table 14 reporting, and dispute resolution with OTAs."
version: 1.0.0
author: Staybird Research
created: 2026-02-25
platforms: [claude-code]
category: gst-compliance
tags: [gst, tcs, ecommerce-operator, reconciliation, hotel, OTA, makemytrip, cleartrip, airbnb, yatra, agoda, travelstack, GSTR-8, GSTR-2B]
risk: safe
---

# GST TCS Reconciliation Skill

Expert guidance for reconciling GST Tax Collected at Source (TCS) from Online Travel Agencies (OTAs) and E-Commerce Operators (ECOs) with a hotel/service provider's books of accounts.

## When to Use This Skill

Use this skill when:
- Reconciling TCS deducted by MakeMyTrip, Cleartrip, Airbnb, Yatra, Agoda, or TravelStack with internal booking records
- Verifying TCS credits in GSTR-2A against GSTR-8 filed by ECOs
- Preparing GSTR-1 Table 14 reporting for supplies made through ECOs
- Investigating missing or incorrect TCS credits in GSTR-2A
- Determining whether an OTA is acting as Agent (TCS applies) vs. Merchant (TCS doesn't apply)
- Resolving disputes with ECOs on TCS amounts
- Creating accounting entries for TCS receipt and utilization

## Legal Framework

### Section 52, CGST Act, 2017 — TCS Obligation

ECOs must collect TCS on **net value of taxable supplies** (gross bookings minus same-month cancellations).

**Current TCS Rate (post July 10, 2024):**
- Intra-state: 0.25% CGST + 0.25% SGST = **0.5% total**
- Inter-state: 0.5% IGST = **0.5% total**

**Pre-July 10, 2024 rate:** 1% (0.5% CGST + 0.5% SGST or 1% IGST)

**Reference:** CBIC Notification No. 15/2024 – Central Tax dated July 10, 2024

### Section 9(5) — ECO as Deemed Supplier

For unregistered suppliers (e.g., unregistered Airbnb hosts), the ECO pays GST itself. In this case, **NO TCS credit** appears in the supplier's GSTR-2A.

---

## ECO Profiles — Quick Reference

### 1. MakeMyTrip (India) Pvt. Ltd.
- **PAN:** AADCM5146R
- **ECO GSTIN Pattern:** XX**AADCM5146R**1C_ (where XX = state code)
- **Filing Status:** Regular GSTR-8 filer
- **Key Issue:** Net value computation after cancellations; multiple state GSTINs

### 2. Cleartrip Private Limited
- **PAN:** AACCC6016B
- **ECO GSTINs:** 04AACCC6016B1CR (Punjab), 38AACCC6016B1CG (Puducherry), and others
- **Related Entity:** Cleartrip Packages & Tours Pvt Ltd (PAN: AAHCC1775A) — separate TCS
- **Key Issue:** Two entities for hotel vs. package bookings; Flipkart group routing

### 3. Airbnb Payments India Pvt. Ltd.
- **PAN:** AANCA6203B
- **ECO GSTINs:** 06AANCA6203B1Z6 (Haryana), 05AANCA6203B1CJ (Uttarakhand), and others
- **Key Issue:** Dual track — registered hosts get TCS credit; unregistered hosts don't (Airbnb pays GST under Section 9(5))

### 4. Yatra Online Limited
- **PAN:** AAACY2602D
- **ECO GSTIN:** 31AAACY2602D1CE (registered Nov 29, 2018)
- **Key Issue:** Corporate + leisure mix; B2B routing for corporate bookings matters

### 5. Agoda Company Pte. Ltd.
- **PAN:** AAQCA5807N (Foreign Company — Singapore)
- **ECO GSTINs:** 16AAQCA5807N1CG, 24AAQCA5807N1CJ, 30AAQCA5807N1CQ, 08AAQCA5807N1CD, and others
- **Key Issue:** FHRAI complaint about commission on GST; RSR pricing model; non-transparent accounting

### 6. TravelStack Tech Limited
- **PAN:** AAFCC6416Q
- **ECO GSTINs:** GSTINs identified end in 'Z' (regular), NOT 'C' (ECO) — likely merchant model
- **Key Issue:** Business model must be confirmed — may be net rate/merchant, not ECO

---

## Core Reconciliation Process

### Step 1: Data Collection (By 15th of month)
1. Download **settlement statements** from each ECO's partner portal
2. Extract: gross bookings, cancellations, net bookings, TCS deducted (by ECO)
3. Download **GSTR-2A data** from GST portal (available after 10th)
4. Filter TCS entries by ECO PAN/GSTIN

### Step 2: GSTIN Identification
Identify the ECO's Tax Collector GSTIN (14th character = 'C') for each state:
- Look up ECO's GSTIN directory in `references/eco-gstin-directory.md`
- Match with the first 2 digits = state code of the ECO (for determining IGST vs CGST+SGST)

### Step 3: Value Matching
Compare:
| Your Books | GSTR-8 (from GSTR-2A) |
|-----------|----------------------|
| Gross bookings | Gross value |
| Less: cancellations (same month) | Net of cancellations |
| **Net taxable value** | **Must match** |
| Net value × 0.5% | TCS amount |

### Step 4: Credit Acceptance (GST Portal)
1. **Services → Returns → TDS and TCS Credit Received**
2. Select period → Review auto-populated entries
3. ACCEPT verified entries | REJECT incorrect entries
4. File (DSC/EVC) → Credit to Electronic Cash Ledger

### Step 5: Accounting Entries
```
At payout from ECO:
Dr. Bank A/c (net settlement)         — settlement received
Dr. TCS Receivable (ECO name)         — TCS deducted
Dr. Commission Expense (ECO name)     — commission deducted
    Cr. Trade Receivable (ECO name)   — full invoice amount

When TCS accepted on portal:
Dr. Electronic Cash Ledger (GST)      
    Cr. TCS Receivable (ECO name)

When GST liability offset:
Dr. Output GST Payable                
    Cr. Electronic Cash Ledger
```

### Step 6: GSTR-1 Table 14 Reporting (From January 2024)
For each ECO, report in Table 14(a): ECO GSTIN, taxable value, and taxes.
- This is **informational only** — does NOT auto-populate GSTR-3B

---

## Mismatch Resolution Guide

| Mismatch Type | Cause | Action |
|--------------|-------|--------|
| ECO value > Your books | ECO counting bookings you cancelled | Request ECO to amend GSTR-8; provide cancellation proof |
| ECO value < Your books | Merchant/net rate model for some bookings | Verify contract; some bookings may be B2B to ECO (no TCS) |
| Old TCS rate (1%) after Jul 10, 2024 | ECO not updated rate | Accept credit; ask ECO to amend |
| No TCS entry | GSTR-8 not filed by ECO | Follow up 3-4 working days after 10th |
| Wrong GSTIN | Your GSTIN not updated with ECO | Update GSTIN on ECO partner portal |
| Agoda RSR / commission on GST | Agoda-specific issue | Document; check FHRAI guidance; adjust commission basis |

---

## Special Cases

### Airbnb — Unregistered Host Properties
If property is rented as residential accommodation (Section 9(5) applies):
- Airbnb pays full GST on your behalf
- **NO TCS credit** in your GSTR-2A for these properties
- Do NOT expect or look for TCS credit for unregistered properties

### TravelStack — Merchant Model Determination
If TravelStack's GSTINs all end in 'Z' (not 'C'):
- Likely merchant/net rate model
- Raise B2B invoice TO TravelStack for contracted room revenue
- No TCS credit to expect in GSTR-2A
- Report in GSTR-1 as B2B sale, not through ECO

### Agoda — RSR/ Commission on GST Issue
- Agoda charges commission on TOTAL (including GST), not pre-tax base
- This is disputed under Indian tax law
- Document every instance; participate in FHRAI complaints if impacted
- For books: Book commission expense on PRE-TAX BASE only; create provision for disputed excess

---

## References

- `references/eco-gstin-directory.md` — Complete GSTIN lookup for all 6 ECOs
- `references/legal-provisions.md` — Full text of Section 52, key notifications
- `references/agoda-fhrai-complaint.md` — FHRAI complaint details and impact
- `references/booking-date-vs-checkin-timing.md` — Timing difference handling guide
- Research files: `/research/gst-tcs-reconciliation/` (complete deep-dive per ECO)

---

## Key Contacts & Resources

| ECO | Partner Portal | TCS Query Channel |
|-----|---------------|------------------|
| MakeMyTrip | partners.makemytrip.com | Account manager / compliance@makemytrip.com |
| Cleartrip | partners.cleartrip.com | Partner support |
| Airbnb | airbnb.co.in/hosting | Host support ticket |
| Yatra | partners.yatra.com | Partner support ticket |
| Agoda | ycs.agoda.com | Account manager |
| TravelStack | [Verify current portal] | Account manager |
