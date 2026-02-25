# MakeMyTrip (India) Pvt. Ltd. — GST TCS Profile & Reconciliation

**Company:** MakeMyTrip (India) Private Limited  
**CIN:** U63010MH2000PTC128711 (approx.)  
**Pan:** AADCM5146R  
**Group:** MakeMyTrip Limited (NASDAQ: MMYT) — also includes Goibibo (ibibo Group)

---

## 1. GST Registration Details

MakeMyTrip (India) Pvt. Ltd. maintains **two types of GSTINs** across states:

### Regular GSTINs (for commission/fee income)
These GSTINs are used for raising commission invoices and collecting service fees from suppliers.

### Tax Collector (ECO) GSTINs
These are the critical ones for TCS purposes. They have 'C' as the 14th character.

**Key ECO GSTINs (Tax Collector type) identified:**

| State | GSTIN | Status |
|-------|-------|--------|
| Chandigarh/Haryana | 06AADCM5146R1CA | Active - Tax Collector ECO |
| Tamil Nadu | 35AADCM5146R1C9 | Active - Tax Collector ECO |
| Others | Multiple state ECO GSTINs | Active |

> **Note:** MakeMyTrip also operates under the **Goibibo** brand. Goibibo's parent ibibo Group may have separate GSTINs. Confirm with your MakeMyTrip partner manager which ECO GSTIN to expect on GSTR-2A for your state.

**State-specific ECO GSTIN format:** XX**AADCM5146R**1C_ (where XX = state code)

### myBiz Platform (Corporate)
MakeMyTrip's B2B platform (myBiz) claims to provide **100% GST Invoice Assurance** including:
- State-specific GSTIN on hotel invoices for corporate ITC claims
- Automated GSTIN validation to reduce booking-time errors

---

## 2. How MakeMyTrip Reports TCS in GSTR-8

### What MakeMyTrip Reports in GSTR-8:

| Field | Description |
|-------|-------------|
| Table 3 | Supplier-wise, state-wise details of taxable supplies made through MMT platform |
| GSTIN of Supplier | Your hotel/service GSTIN (must match exactly) |
| Net Value of Supplies | Gross booking value MINUS cancellations/returns during month |
| TCS Amount | 0.5% (post July 2024) or 1% (pre July 2024) of net value |
| CGST TCS | 0.25% of net value (post July 2024) |
| SGST/IGST TCS | 0.25% SGST (intra-state) or 0.5% IGST (inter-state) |

**Filing Deadline:** 10th of the month following collection  
**Example:** TCS on January bookings → filed in GSTR-8 by February 10

---

## 3. Specific Reconciliation Challenges with MakeMyTrip

### 3.1 Net Value Computation Difference
MakeMyTrip computes TCS on the **net value AFTER CANCELLATIONS within the same month**. This creates timing mismatches because:
- Supplier's GSTR-1 shows gross revenue
- GSTR-8 shows net (after cancellations)
- Cancellations in a different month are adjusted in that month's GSTR-8, NOT retrospectively

**Reconciliation action:** Maintain a monthly booking vs. cancellation tracker segregated by ECO. Cross-verify the net figure reported by MMT in GSTR-8 against your own net.

### 3.2 GST Rate Applied — Hotel Slab Issue
MakeMyTrip computes TCS on the **effective selling price/room tariff** as shown to the customer. However:
- Rooms ≤ ₹7,500: 12% GST (post July 2022)  
- Rooms > ₹7,500: 18% GST
- TCS is on the BASE PRICE, not on the GST amount

**Question for reconciliation:** Does the value in GSTR-8 match YOUR declared taxable value BEFORE GST?

### 3.3 Commission Deduction at Source (Not TCS)
MMT deducts its commission from the payout. This is **NOT TCS**. TCS is a separate amount.

**Example:**
```
Room Rate = ₹10,000 (taxable value)
GST @18% = ₹1,800
Total = ₹11,800
MMT TCS @0.5% = ₹50 (on ₹10,000 taxable value)
MMT Commission @15% = ₹1,500 (deducted from settlement)
Settlement to Hotel = ₹11,800 - ₹50 - ₹1,500 = ₹10,250
```

### 3.4 Multiple State GSTINs of MMT Causing Confusion
If a customer books from Delhi but stays in Mumbai hotel:
- The booking may flow through MMT's Delhi or Maharashtra ECO GSTIN
- TCS may appear under IGST in the supplier's GSTR-2A
- **Action:** Always check both CGST+SGST and IGST TCS entries in GSTR-2A

### 3.5 Amendments in Subsequent Months
MMT can file amendments to prior GSTR-8 in subsequent months. These appear as adjustments (negative or positive) in GSTR-2A for the amendment month.

**Reconciliation action:** Review GSTR-2A not just for the current month but also for retroactive adjustments from MMT.

---

## 4. Books-to-GSTR-8 Reconciliation Template

| Column | Source | Description |
|--------|--------|-------------|
| Booking Month | Internal Records | Month of check-in/service delivery |
| Gross Revenue | GSTR-1 | Total taxable value declared |
| Cancellations | Internal Records | Cancellations within month |
| Net Revenue (Book) | Computed | Gross - Cancellations |
| TCS Reported (GSTR-8) | GSTR-2A | Amount shown by MMT |
| TCS Expected @0.5% | Computed | Net Revenue × 0.5% |
| Variance | Computed | Expected - Reported |
| Variance Reason | Analysis | Timing, rate, GSTIN mismatch |

---

## 5. Key Contact for TCS Dispute with MakeMyTrip

- **Partner Portal:** partners.makemytrip.com (Hotel Extranet)
- **GSTIN for TCS Queries:** Contact your assigned MMT account manager
- **Escalation:** Email to compliance@makemytrip.com (verify current email)
- **Period for Rectification:** MMT can amend GSTR-8 up to September 30 of subsequent year

---

## 6. GSTIN on Settlement Statement

MakeMyTrip's settlement statements to hotels typically show:
- Booking ID
- Check-in and check-out dates
- Room revenue (net of cancellations)
- TCS deducted (separately identified)
- Commission deducted
- Net payment

**Cross-check:** Ensure the ECO GSTIN shown on the settlement statement matches the GSTIN reflected in GSTR-8. Mismatches indicate a state-GSTIN routing issue.
