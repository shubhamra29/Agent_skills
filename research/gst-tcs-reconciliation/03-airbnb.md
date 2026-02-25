# Airbnb Payments India Private Limited — GST TCS Profile & Reconciliation

**Company:** Airbnb Payments India Private Limited  
**PAN:** AANCA6203B  
**Parent:** Airbnb, Inc. (USA — NASDAQ: ABNB)  
**Indian Entity Type:** Private Limited Company incorporated in India for payment processing

---

## 1. GST Registration Details

Airbnb Payments India Private Limited holds **Tax Collector (ECO) GSTINs** in multiple states. Unlike OTAs like MMT or Yatra which primarily deal with hotels, Airbnb hosts include both individuals and commercial properties.

### Key ECO GSTINs Identified:

| State | GSTIN | Registration Type |
|-------|-------|------------------|
| Haryana | 06AANCA6203B1Z6 | Tax Collector (ECO) |
| Uttarakhand | 05AANCA6203B1CJ | Tax Collector (ECO) |
| Other States | Multiple AANCA6203B GSTINs | Tax Collector (ECO) |

---

## 2. Airbnb's Unique GST Model — Two-Track System

Unlike traditional OTAs, Airbnb operates a **dual GST responsibility model** based on host registration status:

### Track 1: Unregistered Hosts
- If a host's annual turnover is below ₹20 lakhs (₹10 lakhs in special category states) and they are **not GST registered**
- Airbnb collects **full GST from guests** and remits directly to tax authorities
- This is the **Section 9(5) model** — Airbnb is the deemed taxpayer
- **Result for service providers/hosts:** NO TCS credit appears; Airbnb has paid the GST on your behalf

### Track 2: GST-Registered Hosts
- Hosts who provide their GSTIN to Airbnb
- Airbnb collects TCS **against the host's GSTIN**
- Host is responsible for paying their own GST
- TCS credit appears in **host's GSTR-2A** from Airbnb's ECO GSTIN
- **Result for service providers/hosts:** TCS credit available in GSTR-2A for claiming

> **Critical for reconciliation:** Determine which track your properties fall under. Only Track 2 results in TCS credit in GSTR-2A.

---

## 3. How Airbnb Reports in GSTR-8 (For Registered Hosts)

### Table 3 — TCS on Supplies by Registered Suppliers

| Field | Value |
|-------|-------|
| Supplier GSTIN | Host's registered GSTIN |
| Gross Value of Bookings | Total room nights × per night rate |
| Cancellations Adjusted | Deducted within same month |
| Net Taxable Value | Gross - Cancellations (within month) |
| TCS @ 0.5% (post Jul 2024) | Net Value × 0.5% |

**Note on Airbnb's Payout Structure:**
- Airbnb charges **service fees** to guests (separate from host payout)
- The host's declared price is the TAXABLE BASE for TCS
- Airbnb's service fee to guests is a separate supply by Airbnb (their own GST liability)

---

## 4. Specific Reconciliation Challenges with Airbnb

### 4.1 Nightly vs. Monthly Computation
Airbnb payouts are typically made **within days of check-out** (not monthly aggregated). However, GSTR-8 is filed monthly. This means:
- Multiple individual payouts during the month are aggregated into one GSTR-8 entry
- **Action:** Download your Airbnb transaction history for the full month → aggregate → compare with GSTR-2A entry

### 4.2 Currency and GST on Foreign Guest Bookings
When foreign tourists book Indian properties on Airbnb:
- Payment may flow in foreign currency (USD, EUR, etc.)
- Airbnb converts to INR and pays host in INR
- TCS is applicable on the **INR equivalent** of the booking value
- **Issue:** Exchange rate used by Airbnb for conversion may differ from your books

### 4.3 Short-Term Rental Classification
Airbnb is predominantly used for **short-term residential rentals**. GST applicability depends on:
- If the property is rented as residential accommodation: May be EXEMPT from GST
- If rented for commercial/tourism purposes: GST applies
- **Reconciliation challenge:** If some bookings are GST-exempt (residential use), TCS should NOT apply on those. However, Airbnb may not always correctly classify co-hosted or hybrid-use properties

### 4.4 Platform Service Fee — Not Included in Host TCS
Airbnb charges guests a **platform service fee** (typically 14-16% of booking). This is NOT part of the host's taxable value. TCS applies ONLY on the host's portion.
- **Verification:** Your taxable value in GSTR-1 should match the amount BEFORE Airbnb's service fee is added
- If the GSTR-8 value appears higher than your expected host earnings, Airbnb may be incorrectly including service fee in host's taxable base

### 4.5 Section 9(5) Properties in Portfolio
If you have a **mix of registered and unregistered properties**, you may receive:
- TCS credit for registered properties (Track 2)
- No TCS credit for unregistered properties (Track 1 — Airbnb pays GST)

**Reconciliation action:** Ensure your books separately account for revenue from each property and its GST treatment.

### 4.6 State Used for ECO GSTIN
Airbnb will use the **state GSTIN** corresponding to the property location. If your property is in Maharashtra, look for TCS in your GSTR-2A under Airbnb's Maharashtra ECO GSTIN.

---

## 5. Airbnb's Communication to Hosts — Getting TCS Data

Airbnb provides to registered Indian hosts:
- **Monthly Transaction Summaries** (downloadable from Airbnb Host Dashboard)
- **Annual Earnings Summary** (for tax filing purposes)
- **TCS Certificate equivalent** — contact Airbnb India support for state-wise TCS breakdowns

**Key Request:** Ask Airbnb to provide: "State-wise monthly GSTR-8 TCS breakdowns for FY ____" — this is needed to reconcile GSTR-2A entries with property-level revenues.

---

## 6. Reconciliation Framework for Airbnb Hosts

| Parameter | Data Source | Frequency |
|-----------|------------|-----------|
| Monthly Booking Revenue per property | Airbnb Host Dashboard | Monthly |
| Cancellations | Airbnb Transaction History | Monthly |
| Expected TCS (0.5% of net) | Computed | Monthly |
| GSTR-2A TCS Credit (Airbnb ECO GSTIN) | GST Portal | Monthly (after 10th) |
| Variance | Computed | Monthly |
| Track 1 Bookings (Unregistered subset) | Airbnb Dashboard | Monthly |
| GST paid by Airbnb under Sec 9(5) | Verify with Airbnb | Annual |

---

## 7. Compositions/ITC Restriction

Hosts using Airbnb **cannot use the GST Composition Scheme** since they are suppliers through an ECO. They must register under Regular GST if turnover exceeds threshold.

---

## 8. Contact for TCS Disputes with Airbnb

- **Airbnb India GST Help:** airbnb.co.in/help/article/1237
- **Host Dashboard:** airbnb.co.in/hosting
- **TCS Query:** Raise a support ticket via Host Dashboard specifying GSTIN, period, and discrepancy amount
- **Airbnb GST Support Email:** Available in the Help Center (verify current contact)
