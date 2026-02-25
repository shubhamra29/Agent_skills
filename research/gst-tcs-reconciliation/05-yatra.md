# Yatra Online Limited — GST TCS Profile & Reconciliation

**Company:** Yatra Online Limited (formerly Yatra Online Pvt Ltd)  
**PAN:** AAACY2602D  
**Status:** Public Listed Company (NASDAQ: YTRA)  
**Headquarters:** Gurugram, Haryana

---

## 1. GST Registration Details

Yatra Online Limited maintains multiple GSTINs for both regular operations and Tax Collector (ECO) functions.

### Regular GSTINs (for Yatra's own services):

| State | GSTIN |
|-------|-------|
| Delhi (Primary) | 07AAACY2602D1ZU |
| Puducherry | 34AAACY2602D1ZX |
| West Bengal | 19AAACY2602D1ZP |
| Kerala | 32AAACY2602D1Z1 |
| Other States | Multiple GSTINs |

### Tax Collector (ECO) GSTIN:

| State | GSTIN | Registration Date | Type |
|-------|-------|-----------------|------|
| Multi-state | 31AAACY2602D1CE | November 29, 2018 | Tax Collector ECO |

> **Key Insight:** Yatra was among the first OTAs to register as Tax Collector ECO when the provisions came into effect on October 1, 2018. The 'CE' suffix in GSTIN 31AAACY2602D1CE is notable — the standard pattern for ECO GSTINs ends in 'C' (14th character). Verify the exact GSTIN from Yatra's partner portal.

---

## 2. Yatra's Business Segments and TCS Impact

### 2.1 Corporate Travel (B2B) — Major Revenue Driver

Yatra is **one of India's largest corporate travel management companies (TMC)**. Its corporate travel platform involves:
- **Companies** (corporate clients) booking through Yatra's platform
- Hotels and airlines as the service providers

**TCS implications for hotel suppliers under corporate segment:**
- Corporate bookings flow through Yatra's platform
- TCS is deducted by Yatra on the hotel's taxable value
- TCS appears in the hotel's GSTR-2A under Yatra's ECO GSTIN
- If the **corporate company** is the actual buyer, Yatra is acting as agent → TCS applies

### 2.2 Leisure Travel (B2C)

Standard OTA model for individual travelers — similar to MakeMyTrip.

### 2.3 MICE Business (Meetings, Incentives, Conferences, Events)

For MICE bookings:
- The booking may be under a customized package arrangement
- TCS may apply only on the accommodation component (if separately identifiable)
- Package as a whole may be classified as "Tour Operator Service" — different GST treatment

---

## 3. Yatra GSTR-8 Filing — What to Expect

### 3.1 Filing Pattern
- Monthly GSTR-8 filed by 10th of next month
- Separate filings for different state GSTINs where Yatra has ECO registration
- Amendments for prior periods possible until September 30 of next year

### 3.2 What Yatra Reports Against Your GSTIN

| Field | Content |
|-------|---------|
| Your GSTIN | Must be correctly provided to Yatra in the hotel extranet |
| Taxable Value | Cumulative room revenue for the month (net of cancellations) |
| TCS CGST | 0.25% (post Jul 2024) |
| TCS SGST/IGST | 0.25% SGST or 0.5% IGST |

### 3.3 Yatra's Special Feature — GST-Guaranteed Invoices
Like MakeMyTrip's myBiz, Yatra's corporate platform claims to ensure proper GSTIN-wise invoice generation for ITC. However, this is for the **end buyer's ITC**, not directly related to TCS on hotel supplies.

---

## 4. Specific Reconciliation Challenges with Yatra

### 4.1 Corporate vs. Leisure Booking Pools

Yatra processes both corporate AND leisure travel. In GSTR-8, these are all combined under a single net figure for each supplier. Your internal records need to similarly aggregate all Yatra-channel bookings (both corporate and leisure) when comparing to GSTR-8.

**Action:** Pull booking reports from Yatra's partner portal segregated by booking date (not check-in date) to align with Yatra's GSTR-8 which is on **collection** basis.

### 4.2 Yatra Corporate — Multiple Subsidiary Bookings

When large corporates book via Yatra, different divisions/subsidiaries of the corporate may stay at your hotel. From your perspective, all these are "Yatra bookings" but from TCS standpoint, all are part of the same supply.

### 4.3 B2B Invoice Issue for Corporate Segment

In corporate travel facilitated by Yatra:
- The **corporate company** (say ABC Pvt Ltd) is the end consumer
- Your hotel may raise a B2B invoice to either:
  a) Yatra Online Limited (if Yatra settles on behalf of corporate), OR
  b) ABC Pvt Ltd (if direct billing allowed by Yatra)

**TCS applies only in scenario (a)** where Yatra collects payment from the corporate and pays the hotel. If the corporate pays the hotel directly, Yatra's TCS does NOT apply.

**Reconciliation action:** Identify which bookings in your records flow through Yatra's payment (TCS applies) vs. direct invoicing to corporate (TCS does NOT apply).

### 4.4 Special Rate Plans and Negotiated Rates

Yatra often offers hotels' preferred corporate rates or negotiated rates. The TCS base should be the **NEGOTIATED RATE** (taxable value), not the best available rate (BAR). Confirm with Yatra's system that the taxable value in GSTR-8 correctly reflects negotiated rates, not inflated BAR rates.

### 4.5 Advance Deposits and Early Settlements

If Yatra makes advance payments or early settlements, TCS timing must align:
- TCS is applicable when **consideration is collected by Yatra from the customer**, not when Yatra pays the hotel
- If a booking is on January 15 (collection by Yatra) for a February stay, TCS goes into January's GSTR-8
- Your hotel's revenue recognition may be in February (check-in date)
- This creates a **permanent timing gap** between TCS appearing in GSTR-2A (January) and you recognizing revenue (February)

---

## 5. Reconciliation Table Template for Yatra

| Parameter | January | February | March |
|----------|---------|----------|-------|
| Yatra Bookings (Collection Date) | | | |
| Cancellations (Same Month) | | | |
| Net Value per Books | | | |
| GSTR-8 Value (from GSTR-2A) | | | |
| Variance | | | |
| Expected TCS (0.5%) | | | |
| GSTR-2A TCS Credit | | | |
| TCS Variance | | | |
| Accepted in TCS Portal? | Yes/No | Yes/No | Yes/No |

---

## 6. Yatra B2B Portal and Data Downloads

**Yatra Partner/Hotel Portal:** yatra.com/hoteladmin or local extranet
- Monthly booking summary by collection date
- Cancellation reports
- Settlement statements (showing TCS deductions separately)

**If TCS is deducted but NOT appearing in GSTR-2A:**
- Yatra may not have filed GSTR-8 for that period → Follow up with Yatra
- Yatra may have used wrong GSTIN for your property → Verify on their system
- GSTN processing delay → Check again after 15th of the month

---

## 7. Contact Information

- **Yatra Hotel Partner Support:** partners.yatra.com  
- **Yatra Corporate Desk:** corporate.yatra.com  
- **Finance/TCS Queries:** Raise support ticket on partner portal with "GST TCS Query" subject  
- **GST GSTIN Updation:** Update your GSTIN in Yatra's extranet to ensure correct TCS credit
