# Cleartrip Private Limited — GST TCS Profile & Reconciliation

**Company:** Cleartrip Private Limited  
**PAN:** AACCC6016B  
**Ownership:** Cleartrip is now a subsidiary of Flipkart (Walmart Group) since 2021

---

## 1. GST Registration Details

Cleartrip Private Limited operates as a **Tax Collector (Electronic Commerce Operator)** across multiple states.

### Key ECO GSTINs (Tax Collector type — 14th character 'C'):

| State | GSTIN | Type |
|-------|-------|------|
| Punjab | 04AACCC6016B1CR | Tax Collector – ECO |
| Pondicherry | 38AACCC6016B1CG | Tax Collector – ECO |
| Other States | Multiple | Regular / ECO |

### Key Regular GSTINs (Cleartrip's own operations):

| State | GSTIN | Type |
|-------|-------|------|
| Maharashtra | 27AACCC6016B1Z8 | Regular taxpayer |
| Karnataka | 29AACCC6016B1Z4 | Regular taxpayer |
| Delhi | 07AACCC6016B1CL | Regular taxpayer |
| Himachal Pradesh (Cleartrip Packages & Tours Pvt Ltd) | 02AAHCC1775A1Z9 | Regular taxpayer |

> **CAUTION:** Cleartrip Packages & Tours Private Limited is a **separate legal entity** with a different PAN (AAHCC1775A). If you have bookings under Cleartrip Packages, the TCS may appear under this entity's GSTIN, not Cleartrip Private Limited's GSTIN.

---

## 2. How Cleartrip Reports TCS in GSTR-8

### Scope of Services Covered by TCS

| Service Type | TCS Applicable? | Notes |
|-------------|-----------------|-------|
| Hotel Bookings (Registered Hotel) | Yes | TCS @0.5% on net taxable value |
| Hotel Bookings (Unregistered Hotel) | No TCS | Cleartrip pays GST under Sec 9(5) |
| Flight Bookings | Generally No | Airlines are direct taxpayers; Cleartrip acts as IATA agent |
| Holiday Packages | Yes (for hotel component) | Complex allocation required |
| Activity/Experience Bookings | Yes | If supplier is registered |

### Historical Confusion — IATA Agent Issue
When TCS provisions were first implemented (October 2018), there was considerable confusion among OTAs including Cleartrip about their role as IATA agents for flight bookings. The clarification eventually was:
- For **airline tickets**, the airline itself pays GST on its service; Cleartrip collects convenience fees (on which it pays its own GST) → **TCS is NOT typically applicable to the airline's portion**
- For **hotel/package** components facilitated through the platform, **TCS applies**

---

## 3. Specific Reconciliation Challenges with Cleartrip

### 3.1 Flipkart Integration and Payment Flow
Post-Flipkart acquisition, Cleartrip's payment systems may route through multiple entities. Check:
- Whether the TCS in GSTR-2A is from "Cleartrip Private Limited" or any related Flipkart entity
- Verify the PAN of the ECO shown in GSTR-2A matches AACCC6016B

### 3.2 Cleartrip Packages vs. Cleartrip Hotel-Only Bookings
If you receive bookings under **Cleartrip Packages**, the GSTR-8 filing entity may be **Cleartrip Packages & Tours Private Limited** (PAN: AAHCC1775A), not Cleartrip Private Limited. This means TCS will appear under a different GSTIN in GSTR-2A.

**Reconciliation action:** 
- Check your settlement statement header — which company name is shown?
- Look for TCS credit entries under BOTH Cleartrip Private Limited GSTINs AND Cleartrip Packages GSTINs

### 3.3 State-Specific GSTIN for Intra-State vs. Inter-State
When a hotel in Karnataka receives a booking where the Cleartrip ECO GSTIN used is Karnataka-based:
- TCS = CGST 0.25% + SGST 0.25% (intra-state)

When the Cleartrip ECO GSTIN used is from another state:
- TCS = IGST 0.5% (inter-state)

The hotel supplier must ensure that the correct tax head (CGST+SGST vs IGST) appears in GSTR-2A.

### 3.4 Commission Structure and Merchant Model
Cleartrip operates on two models:
1. **Marketplace Model:** Cleartrip collects from customer → remits to hotel → TCS applicable (Section 52)
2. **Merchant Model:** Cleartrip buys inventory at net rate → sells at higher price → TCS NOT applicable (Cleartrip is the principal supplier, not an ECO for that transaction)

**Critical reconciliation point:** Determine under which model your bookings are flowing. In the Merchant Model, TCS will NOT appear in your GSTR-2A.

---

## 4. Books-to-GSTR-8 Reconciliation Template for Cleartrip

| Column | Source |
|--------|--------|
| Month | Tax Period |
| Bookings via Cleartrip | Internal Reports (from Cleartrip Extranet) |
| Cancellations in Same Month | Internal Records |
| Net Taxable Value (Books) | Revenue ledger |
| GSTR-8 Value (Cleartrip) | GSTR-2A download |
| Difference | Computed |
| Difference Reason | Analysis |
| TCS Expected @0.5% | Net value × 0.5% |
| TCS Reported | From GSTR-2A |
| Shortfall/Excess | Computed |

---

## 5. Settlement Statement Cross-Verification

Cleartrip's partner settlement statements should show:
- Booking Reference Number
- Check-in Date
- Taxable value of accommodation
- TCS deducted (showing GSTIN of deducting entity)
- GST charged to customer (if visible)
- Commission/net payment

**Key verification:** The **TCS deducted line** in the settlement should show the ECO GSTIN from which TCS will appear in GSTR-2A. If this field is absent or shows a different entity, your GSTR-2A reconciliation will not match.

---

## 6. Contact for TCS Disputes

- **Cleartrip Partner Portal:** partners.cleartrip.com
- **Cleartrip IATA Agency Relations:** For flight booking TCS clarifications
- **Dispute Timeline:** Amendments to GSTR-8 are possible until September 30 after the financial year end
