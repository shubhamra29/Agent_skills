# ECO GSTIN Directory — For TCS Reconciliation

**Last Updated:** February 2026  
**Purpose:** Quick reference for identifying the correct ECO GSTIN in GSTR-2A when reconciling TCS credits

---

## How to Use This Directory

1. Identify which ECO made the booking (MakeMyTrip, Cleartrip, etc.)
2. Find the state code (first 2 digits of GSTIN) matching the **ECO's registration state** relevant to the booking flow
3. Cross-reference with GSTR-2A entries to find TCS credit
4. **Key rule:** ECO GSTIN ends in 'C' (14th character), NOT 'Z'

---

## State Codes Reference

| State Code | State/UT |
|-----------|---------|
| 01 | Jammu & Kashmir |
| 02 | Himachal Pradesh |
| 03 | Punjab |
| 04 | Chandigarh |
| 05 | Uttarakhand |
| 06 | Haryana |
| 07 | Delhi |
| 08 | Rajasthan |
| 09 | Uttar Pradesh |
| 10 | Bihar |
| 11 | Sikkim |
| 12 | Arunachal Pradesh |
| 13 | Nagaland |
| 14 | Manipur |
| 15 | Mizoram |
| 16 | Tripura |
| 17 | Meghalaya |
| 18 | Assam |
| 19 | West Bengal |
| 20 | Jharkhand |
| 21 | Odisha |
| 22 | Chhattisgarh |
| 23 | Madhya Pradesh |
| 24 | Gujarat |
| 26 | Dadra & Nagar Haveli and Daman & Diu |
| 27 | Maharashtra |
| 28 | Andhra Pradesh (old) |
| 29 | Karnataka |
| 30 | Goa |
| 31 | Lakshadweep |
| 32 | Kerala |
| 33 | Tamil Nadu |
| 34 | Puducherry |
| 35 | Andaman & Nicobar Islands |
| 36 | Telangana |
| 37 | Andhra Pradesh |
| 38 | Ladakh |

---

## MakeMyTrip (India) Pvt. Ltd. — ECO GSTINs

**PAN:** AADCM5146R  
**ECO GSTIN Pattern:** [State Code]AADCM5146R1C[Suffix]

| State | Known ECO GSTIN | Status |
|-------|----------------|--------|
| Haryana (06) | 06AADCM5146R1CA | Active (confirmed) |
| Tamil Nadu (35) | 35AADCM5146R1C9 | Active (confirmed) |
| Other states | [State]AADCM5146R1C_ | Check GSTN portal |

**How to verify:** Search "AADCM5146R" on gstin.gov.in to get full list of active GSTINs.

> **Note:** Also includes Goibibo (ibibo Group) under MakeMyTrip's umbrella. Verify if separate GSTINs are used.

---

## Cleartrip Private Limited — ECO GSTINs

**PAN:** AACCC6016B  
**ECO GSTIN Pattern:** [State Code]AACCC6016B1C[Suffix]

| State | Known ECO GSTIN | Status |
|-------|----------------|--------|
| Punjab (04) | 04AACCC6016B1CR | Active – ECO (confirmed) |
| Puducherry (38) | 38AACCC6016B1CG | Active – ECO (confirmed) |
| Other states | [State]AACCC6016B1C_ | Check GSTN portal |

### Cleartrip Packages & Tours Pvt Ltd (SEPARATE ENTITY)

**PAN:** AAHCC1775A  
**Known GSTIN:** 02AAHCC1775A1Z9 (Himachal Pradesh — regular, not ECO)

> **Alert:** Check whether your booking is under Cleartrip or Cleartrip Packages by reviewing the settlement statement header.

---

## Airbnb Payments India Private Limited — ECO GSTINs

**PAN:** AANCA6203B  
**ECO GSTIN Pattern:** [State Code]AANCA6203B1[Suffix]

| State | Known GSTIN | Type | Status |
|-------|------------|------|--------|
| Haryana (06) | 06AANCA6203B1Z6 | Regular/ECO | Active (confirmed) |
| Uttarakhand (05) | 05AANCA6203B1CJ | Tax Collector ECO | Active (confirmed) |
| Other states | [State]AANCA6203B1_ | Check GSTN portal | — |

> **Note:** Some Airbnb GSTINs may end in 'Z' (regular taxpayer), indicating that state may not have a dedicated ECO registration. TCS for intra-state bookings in those states may be filed under IGST from another state's ECO GSTIN.

---

## Yatra Online Limited — ECO GSTINs

**PAN:** AAACY2602D  
**ECO GSTIN Pattern:** [State Code]AAACY2602D1C[Suffix]

| State | Known ECO GSTIN | Registration Date | Status |
|-------|----------------|-----------------|--------|
| Multi-state | 31AAACY2602D1CE | November 29, 2018 | Active – ECO (confirmed) |
| Delhi (07) | 07AAACY2602D1ZU | Regular taxpayer | Active |

> **Note:** "31" = Lakshadweep code. This may be a pan-India ECO registration. Verify on GST portal for state-specific GSTINs.

---

## Agoda Company Pte. Ltd. — ECO GSTINs

**PAN:** AAQCA5807N  
**Foreign Company (Singapore)**  
**ECO GSTIN Pattern:** [State Code]AAQCA5807N1C[Suffix]

| State | Known ECO GSTIN | Registration Date | Status |
|-------|----------------|-----------------|--------|
| Tripura (16) | 16AAQCA5807N1CG | March 19, 2021 | Active – ECO |
| Gujarat (24) | 24AAQCA5807N1CJ | 2021 | Active – ECO |
| Goa (30) | 30AAQCA5807N1CQ | March 16, 2021 | Active |
| Rajasthan (08) | 08AAQCA5807N1CD | 2021 | Active – ECO |

### Separate Entity — Agoda International India Pvt Ltd (Local Subsidiary)

**PAN:** AAKCA7646M  
**GSTIN:** 27AAKCA7646M1Z1 (Maharashtra)  

> **For TCS purposes:** Look for AAQCA5807N GSTINs, NOT AAKCA7646M.

---

## TravelStack Tech Limited — GSTINs

**PAN:** AAFCC6416Q  
**Status:** Appears to be REGULAR taxpayer, NOT ECO Tax Collector

| State | Known GSTIN | Type | Status |
|-------|------------|------|--------|
| West Bengal (19) | 19AAFCC6416Q1Z3 | Regular | Active |
| Maharashtra (27) | 27AAFCC6416Q1Z6 | Regular | Active |
| Himachal Pradesh (02) | 02AAFCC6416Q1ZI | Regular | Active |
| Andhra Pradesh (37) | 37AAFCC6416Q1Z5 | Regular | Active |
| Uttar Pradesh (09) | 09AAFCC6416Q1Z4 | Regular | Active |

> **CRITICAL:** No 'C' suffix GSTINs identified for TravelStack. They are likely NOT acting as ECO Tax Collector. TCS reconciliation with TravelStack likely not applicable. Verify business model — they may be a merchant OTA or tour operator buying accommodation at net rates.

---

## How to Search for ECO GSTINs

**Official GST Portal:** https://www.gst.gov.in  
→ Search Taxpayer → By GSTIN/UIN → Enter known GSTIN

OR

**Third-party GSTIN lookup:**
- gstzen.in
- cleartax.in/gst/gstin-search
- piceapp.com/gstin-search

**Search by PAN:** Enter PAN to see all associated GSTINs (all states)

---

## Verification Checklist

Before looking for TCS in GSTR-2A:
- [ ] Have you provided your correct GSTIN to the ECO in their partner portal?
- [ ] Does the state code in the ECO's GSTIN match expectations?
- [ ] Has the ECO confirmed their GSTR-8 filing status for the period?
- [ ] Have you waited until after the 10th-11th of the month for GSTR-2A to update?
- [ ] Have you checked whether TCS type is CGST+SGST (intra-state) or IGST (inter-state)?
