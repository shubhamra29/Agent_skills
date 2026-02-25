# GST TCS Reconciliation: Framework Overview

**Research Date:** February 25, 2026  
**Scope:** GST Tax Collected at Source (TCS) for Travel & Hospitality Sector ECOs

---

## 1. Legal Framework

### 1.1 Section 52 of CGST Act, 2017

Section 52 mandates **every Electronic Commerce Operator (ECO)** to collect tax at source on the **net value of taxable supplies** made through their platform by other registered suppliers — but only when the consideration for such supplies is collected by the ECO.

**Key definitions:**
- **E-commerce Operator (ECO):** Any person who owns, operates, or manages a digital or electronic facility or platform for electronic commerce.
- **Net Value of Taxable Supplies:** Aggregate value of taxable supplies made through the operator, **minus** the value of any supplies returned during the month.

### 1.2 TCS Rates (Historical & Current)

| Period | CGST Rate | SGST/UTGST Rate | IGST Rate | Total |
|--------|-----------|-----------------|-----------|-------|
| Oct 1, 2018 – Jul 9, 2024 | 0.5% | 0.5% | 1% | 1% |
| **Jul 10, 2024 onwards** | **0.25%** | **0.25%** | **0.5%** | **0.5%** |

> **Notification:** CBIC Notification No. 15/2024 – Central Tax dated July 10, 2024 reduced TCS from 1% to 0.5%.

### 1.3 Section 9(5) Exception — ECO as Deemed Supplier

For certain services where suppliers are **unregistered**, the ECO itself is liable to pay GST (not just collect TCS). This applies to:
- Hotel accommodation/clubs (unregistered suppliers)
- Passenger transport — radio taxis, motor cabs, motorcycles
- Housekeeping services (plumbing, carpentry, etc.)

> **Critical distinction for reconciliation:** If ECO is paying GST under Section 9(5), TCS does NOT apply. The supplier gets NO TCS credit in this case.

---

## 2. Compliance Calendar

| Return | Filed By | Due Date | Content |
|--------|----------|----------|---------|
| GSTR-8 | ECO | 10th of next month | Monthly TCS statement |
| GSTR-9B | ECO | December 31 | Annual TCS statement |
| TCS Credit Return | Supplier | Before GSTR-3B filing | Accept/reject TCS credits |
| GSTR-1 Table 14 | Supplier | 11th of next month | ECO-wise sales summary (wef Jan 2024) |

---

## 3. Flow of TCS Mechanism

```
Customer pays ECO
      ↓
ECO collects full amount (Room rate + GST + TCS)
      ↓
ECO pays Supplier: Amount net of TCS
      ↓
ECO files GSTR-8 (by 10th of next month)
      ↓
TCS credit auto-appears in Supplier's GSTR-2A
      ↓
Supplier accepts credit in "TDS & TCS Credit Received" section
      ↓
TCS amount credited to Supplier's Electronic Cash Ledger
      ↓
Supplier uses credit to pay GST in GSTR-3B
```

---

## 4. ECO GSTIN Structure — Key Identifier

ECOs maintain **two categories of GSTINs**:
1. **Regular GSTIN** (14th character = 'Z'): For their own outward supplies (commission income, platform fees)
2. **ECO/Tax Collector GSTIN** (14th character = 'C'): For collecting TCS from suppliers

> **Alert for reconciliation:** The TCS will be deposited under the ECO's **Tax Collector GSTIN** (ending in 'C'). Ensure you are matching with the correct GSTIN type.

---

## 5. New Reporting Requirements (Effective January 2024)

### GSTR-1 Table 14 — Supplier's Obligation
Suppliers must now report ECO-GSTIN-wise summary of supplies:
- **Table 14(a):** Supplies on which ECO collects TCS under Section 52 (informational only, does NOT auto-populate GSTR-3B)
- **Table 14(b):** Supplies where ECO pays tax under Section 9(5) → auto-populates Table 3.1.1(ii) of GSTR-3B

### GSTR-1 Table 15 — ECO's Obligation  
ECO reports supplies on which it is the deemed supplier under Section 9(5):
- B2B: Supplies between registered parties
- URP2B: Supplies from unregistered to registered parties

---

## 6. Credit Claim Process — Step-by-Step

1. Log into GST portal → **Services → Returns → TDS and TCS Credit Received**
2. Select the relevant **financial year and tax period**
3. Review auto-populated TCS entries from ECO's GSTR-8
4. **Accept or Reject** each entry individually
   - Rejected entries go back to ECO for amendment
   - Once filed, actions are **irreversible**
5. **File** the "TDS and TCS Credit Received" statement (DSC or EVC)
6. Accepted TCS credit appears in **Electronic Cash Ledger**
7. Use balance to offset GST liability in GSTR-3B
8. Claim refund if excess balance remains

---

## 7. Invoice Management System (IMS) — October 2024

Effective October 1, 2024, the Invoice Management System (IMS) was introduced to:
- Enhance ITC claims and reduce discrepancies
- Allow dynamic acceptance/rejection of invoices
- Further automate GSTR-2B population

---

## References
- Section 52, CGST Act, 2017
- CGST Notification 15/2024 (TCS Rate Reduction)
- GSTR-8 filing instructions: gst.gov.in
- CBIC Circular on ECO TCS compliance
