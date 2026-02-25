# Comprehensive GST TCS Reconciliation Analysis — All ECOs

**Purpose:** Master reconciliation guide for service providers working with Airbnb, Cleartrip, TravelStack, Yatra, Agoda, and MakeMyTrip  
**Applicable FY:** 2024-25 (rates updated post July 10, 2024)

---

## 1. ECO Master Reference Table

| ECO Name | Legal Entity | PAN | Key ECO GSTIN Pattern | TCS Rate (Post Jul 2024) | Model |
|----------|-------------|-----|----------------------|--------------------------|-------|
| MakeMyTrip | MakeMyTrip (India) Pvt. Ltd. | AADCM5146R | XX**AADCM5146R**1C_ | 0.5% | Agency |
| Cleartrip | Cleartrip Private Limited | AACCC6016B | 04**AACCC6016B**1CR, 38**AACCC6016B**1CG | 0.5% | Agency/Merchant |
| Airbnb | Airbnb Payments India Pvt. Ltd. | AANCA6203B | 06**AANCA6203B**1Z6, 05**AANCA6203B**1CJ | 0.5% | Agency (Sec 52) or Sec 9(5) |
| Yatra | Yatra Online Limited | AAACY2602D | 31**AAACY2602D**1CE | 0.5% | Agency + Corporate |
| Agoda | Agoda Company Pte. Ltd. | AAQCA5807N | XX**AAQCA5807N**1C_ | 0.5% | Contested (RSR model) |
| TravelStack | TravelStack Tech Limited | AAFCC6416Q | **Unclear — verify** | To be confirmed | Uncertain |

---

## 2. Master Reconciliation Process Flow

### Phase 1: Data Collection (By 15th of each month)

```
For each ECO:
1. Download settlement/payout statement from partner portal
2. Extract total bookings, cancellations, net bookings by collection date
3. Note any TCS amount shown in settlement statement
4. Access GSTR-2A on GST portal (available after 10th-11th)
5. Download TCS entries from GSTR-2A section
6. Export to Excel for comparison
```

### Phase 2: GSTIN-Level Matching

For each ECO, identify the correct TCS GSTIN to look for in GSTR-2A:

| Your Hotel State | Expected ECO GSTIN | Tax Type |
|-----------------|-------------------|----------|
| Same state as ECO registration | State-specific ECO GSTIN | CGST + SGST |
| Different state from ECO | ECO may use pan-India registration or opposite state GSTIN | IGST |

> **Rule of Thumb:** The ECO's GSTR-8 filing GSTIN determines which state code (first 2 digits) appears in your GSTR-2A. If a booking flows through MMT's Karnataka GSTIN and your hotel is in Karnataka, you'll see CGST+SGST. If it's through MMT's Delhi GSTIN for a Karnataka hotel, you'll see IGST.

### Phase 3: Value Matching

#### Column-by-Column Reconciliation:

| Your Books | GSTR-8 (via GSTR-2A) | Expected Match? |
|-----------|---------------------|-----------------|
| Gross bookings from [ECO] | Gross value in GSTR-8 | Should match |
| Less: Same-month cancellations | Already netted in GSTR-8 | — |
| **Net taxable value** | **Net value in GSTR-8** | **Must match** |
| TCS @0.5% of net value | TCS amount in GSTR-8 | Must match |

#### Common Reasons for Mismatch:

| Mismatch Type | Root Cause | Resolution |
|--------------|-----------|------------|
| ECO value > Your records | ECO counting bookings you have already cancelled | Check cancellation records; raise with ECO for amendment |
| ECO value < Your records | ECO using net rate model (merchant), not counting some bookings | Verify business model; some bookings may be direct B2B |
| TCS rate mismatch | ECO applying old rate (1%) after July 10, 2024 | Raise with ECO; they should amend GSTR-8 |
| GSTIN mismatch | Wrong GSTIN provided to ECO | Update GSTIN in ECO's partner portal immediately |
| Missing TCS entry | ECO has not filed GSTR-8 for the period | Follow up with ECO finance team |
| Duplicate TCS entry | ECO filed twice accidentally | Request amendment from ECO |

### Phase 4: Credit Acceptance

**On GST Portal:**
1. Go to: Services → Returns → TDS and TCS Credit Received
2. Select: Financial Year and Tax Period
3. View: Auto-populated TCS entries from each ECO's GSTR-8
4. Action per entry:
   - **ACCEPT** if the amount matches your records
   - **REJECT** if the amount is wrong (goes back to ECO for amendment)
5. File the TCS Credit Received return (DSC/EVC)
6. Check: Electronic Cash Ledger for credit reflection

**CAUTION:** Once you ACCEPT, you cannot reject later. Only accept amounts you have verified.

### Phase 5: Book Adjustments

After accepting TCS credit:
1. Debit Electronic Cash Ledger (Asset) → Credit TCS Receivable account (already booked)
2. When filing GSTR-3B, use Electronic Cash Ledger to pay: CGST, SGST, IGST liabilities
3. Surplus Electronic Cash Ledger balance → Apply for REFUND under GST rules

---

## 3. Accounting Treatment — Service Provider's Books

### At Time of Booking (Revenue Recognition)

```
Dr. Trade Receivable (ECO/OTA Name)    ₹XXX
    Cr. Revenue from Operations          ₹XXX
    Cr. GST Payable (CGST/SGST/IGST)    ₹XXX
```

> Note: Recognize full room revenue even though ECO will settle net of TCS and commission

### At Time of Settlement/Payout from ECO

```
Dr. Bank Account                         ₹XXX (net settlement received)
Dr. TCS Receivable - [ECO Name]         ₹XXX (TCS deducted by ECO)
Dr. Commission Expense - [ECO Name]     ₹XXX (OTA commission)
Dr. Input Tax Credit Receivable         ₹XXX (GST on commission — if payable)
    Cr. Trade Receivable – [ECO Name]   ₹XXX (full invoice amount)
```

### At Time of TCS Credit Acceptance on GST Portal

```
Dr. Electronic Cash Ledger (GST portal)  ₹XXX
    Cr. TCS Receivable - [ECO Name]      ₹XXX
```

### At Time of GST Liability Offset (GSTR-3B)

```
Dr. GST Payable (Output Tax)             ₹XXX
    Cr. Electronic Cash Ledger            ₹XXX
```

---

## 4. GSTR-1 Reporting Alongside TCS (New Jan 2024 Requirement)

### What YOU must file in GSTR-1 Table 14:

**Table 14(a) — For each ECO collecting TCS (Section 52):**

| ECO GSTIN | Trade Name | Taxable Value | IGST | CGST | SGST | Cess |
|-----------|-----------|-------------|------|------|------|------|
| AADCM5146R... (MMT) | MakeMyTrip | ₹X | ₹X | ₹X | ₹X | — |
| AACCC6016B... (Cleartrip) | Cleartrip | ₹X | ₹X | ₹X | ₹X | — |
| AAQCA5807N... (Agoda) | Agoda | ₹X | ₹X | ₹X | ₹X | — |
| AAACY2602D... (Yatra) | Yatra Online | ₹X | ₹X | ₹X | ₹X | — |
| AANCA6203B... (Airbnb) | Airbnb Payments | ₹X | ₹X | ₹X | ₹X | — |

**Key Note:** Table 14(a) entries are **informational only** and do NOT auto-populate GSTR-3B. All your output liability is still declared separately in GSTR-3B Tables.

**Table 14(b) — For Section 9(5) bookings (if Airbnb pays GST for unregistered hosts):**
- Only applicable if you are unregistered and Airbnb is paying GST under Section 9(5) on your behalf
- If you ARE registered: Not applicable to Table 14(b)

---

## 5. Annual Reconciliation (GSTR-9 Level)

### Year-End Reconciliation Checklist:

| Parameter | Source | Target |
|----------|--------|--------|
| Total revenue via OTAs (all 6 ECOs) | Books/P&L | GSTR-9 Table 5 (Outward Supplies) |
| Total TCS collected by OTAs | Sum of GSTR-2A TCS entries (accepted) | GSTR-9C  |
| TCS credit used vs. surplus | Electronic Cash Ledger statement | GSTR-9 supplementary |
| GSTR-8 vs. GSTR-2A match | Annual report | Ensure no gaps |

### ECO Annual Statement (GSTR-9B by ECO)
Each ECO must file an annual statement (GSTR-9B) by December 31. This is a useful cross-check document — request a copy from your OTA partners.

---

## 6. Special Situations

### 6.1 Multiple Properties, Multiple GSTINs
If your business has multiple properties across states with different GSTINs (e.g., hotel in Delhi GSTIN, hotel in Goa GSTIN):
- Ensure EACH property's GSTIN is correctly updated with EACH ECO for that property
- TCS will appear separately under each GSTIN in GSTR-2A
- CROSS-PROPERTY reconciliation: Verify TCS credit mapped to correct property GSTIN

### 6.2 Booking Date vs. Check-In Date vs. Collection Date
TCS is on the **collection date** (when ECO collects from customer), not on check-in or service delivery date.

| Scenario | Booking Date | Check-In | Collection Date | TCS Month |
|---------|-------------|----------|----------------|-----------|
| Advance booking | January | March | January (at booking) | January |
| Pay-at-property | January | March | March (at check-in) | March |
| Pay later | January | March | February (e.g., 30 days before) | February |

**Reconciliation challenge:** Your revenue (P&L) books the transaction in March (check-in month), but TCS appears in January's GSTR-2A. This leads to:
- TCS credit available in January
- Revenue only recognized in March
- Solution: Book a TCS Receivable in January; offset against revenue in March

### 6.3 GST Rate Mismatch — Pre and Post July 10, 2024

If any ECO continues filing GSTR-8 at 1% after July 10, 2024 (instead of 0.5%):
- You'll receive EXCESS TCS credit in your Electronic Cash Ledger
- This is technically the ECO's error  
- You can ACCEPT and use the extra credit (it will be refundable)
- ECO will need to file an amendment to correct the rate
- **Practical action:** Accept the excess credit; coordinate with ECO to amend and your books to reflect the correct net basis

### 6.4 Cancelled Bookings in Same Month
Net Value = Gross Bookings - Cancellations (WITHIN the same GSTR-8 month)

Example:
```
Bookings (January) through MMT: ₹10,00,000
Cancellations (January) through MMT: ₹1,50,000
Net Value in MMT's GSTR-8: ₹8,50,000
TCS in GSTR-8: ₹4,250 (0.5% of ₹8,50,000)
```

If cancellation of January booking comes in February:
```
February GSTR-8 Net Value: ₹X,XX,000 - ₹1,50,000 (January cancellation adjustment)
```

---

## 7. Red Flags Requiring Immediate Action

| Red Flag | Action |
|---------|--------|
| TCS in GSTR-2A but LESS than expected | Verify if ECO has filed amended GSTR-8; raise dispute |
| TCS in GSTR-2A but MORE than expected | Verify if extra bookings credited; accept only verified amount |
| NO TCS entry from an ECO for a month with active bookings | Check if ECO filed GSTR-8; follow up; check if merchant model applies |
| GSTIN in GSTR-2A does not match expected ECO GSTIN | May be a group entity or GSTIN routing issue; verify |
| RSR/commission on GST (Agoda specific) | Document and raise with FHRAI; adjust books to reflect actual pre-tax commission base |
| TCS rate is 1% (post July 10, 2024) | ECO didn't update rate; accept credit; coordinate for ECO amendment |

---

## 8. Software/Tools for Automation

| Tool | Function | Applicable For |
|------|---------|---------------|
| GST filing software (Tally/Zoho Books/Cleartax) | GSTR-1 Table 14 auto-fill | All ECOs |
| Excel reconciliation template | Month-wise ECO vs GSTR-2A comparison | All ECOs |
| GSTN APIs (via tax software) | Auto-download GSTR-2A data | Bulk reconciliation |
| OTA Partner Portals | Booking/cancellation data | MMT, Cleartrip, Yatra, Agoda, Airbnb |
| IMS (Invoice Management System, from Oct 2024) | Dynamic accept/reject management | All ECOs |

---

## 9. Summary: ECO-Specific Risk Level for Reconciliation

| ECO | Reconciliation Complexity | Key Risk |
|-----|--------------------------|---------|
| MakeMyTrip | Medium | Timing of cancellations; MMT's computation of net value |
| Cleartrip | Medium-High | Two entities (Cleartrip + Cleartrip Packages); merchant model confusion |
| Airbnb | High | Dual track (registered/unregistered); Sec 9(5) for unregistered hosts |
| Yatra | Medium | Corporate + leisure mix; B2B invoice routing confusion |
| Agoda | Very High | FHRAI complaint; commission on GST; merchant/RSR model; foreign ECO |
| TravelStack | Unknown | Business model unclear; may not be ECO at all |
