# GST TCS Reconciliation Research — Index

**Prepared:** February 25, 2026  
**Scope:** GST Tax Collected at Source for Travel & Hospitality ECOs  
**ECOs Covered:** MakeMyTrip, Cleartrip, Airbnb, Yatra, Agoda, TravelStack

---

## Research Files

| File | Contents |
|------|---------|
| `00-overview.md` | Legal framework, Section 52, TCS rates, compliance calendar, flow diagram |
| `01-makemytrip.md` | MakeMyTrip GSTIN details, GSTR-8 reporting, reconciliation challenges |
| `02-cleartrip.md` | Cleartrip GSTIN details, two-entity issue (Cleartrip + Cleartrip Packages), merchant model |
| `03-airbnb.md` | Airbnb dual-track model (registered vs. unregistered hosts), Sec 9(5) implications |
| `04-agoda.md` | Agoda's foreign company status, FHRAI complaint, RSR pricing model issues |
| `05-yatra.md` | Yatra's corporate travel focus, B2B invoice routing, timing challenges |
| `06-travelstack.md` | TravelStack's unclear ECO status, merchant model analysis, action items |
| `07-comprehensive-reconciliation.md` | Master reconciliation process, accounting entries, GSTR-1 Table 14, annual checklist |

---

## Key Findings Summary

### 1. TCS Rate Change (Post July 10, 2024)
All ECOs now collect TCS at **0.5%** (down from 1%). Verify your ECOs have updated their rates.

### 2. Business Model Determines TCS Applicability
- **Agency Model** (ECO collects on behalf of supplier): TCS applies under Section 52
- **Merchant Model** (ECO buys at net rate): TCS does NOT apply; hotel raises B2B invoice to ECO

### 3. Section 9(5) Exception
For unregistered suppliers (e.g., unregistered Airbnb hosts): ECO itself pays GST. No TCS credit for the supplier.

### 4. GSTR-1 Table 14 (New from January 2024)
All service providers must now report their ECO-channel supplies in Table 14(a) of GSTR-1. This is informational and does NOT auto-populate GSTR-3B.

---

## ECO Risk & Complexity Summary

| ECO | Complexity | Primary Risk |
|-----|-----------|-------------|
| MakeMyTrip | Medium | Cancellation timing; multiple state GSTINs |
| Cleartrip | Medium-High | Two-entity issue; Flipkart integration; merchant model ambiguity |
| Airbnb | High | Dual track system; Sec 9(5); foreign currency; residential vs. commercial |
| Yatra | Medium | Corporate booking routing; B2B invoice direction |
| **Agoda** | **Very High** | **FHRAI complaint active; RSR model (commission on GST); foreign company; non-transparent accounting** |
| TravelStack | Unknown | Business model unclear; likely merchant model (NO TCS) |

---

## Immediate Action Items

1. **Verify GSTIN is correctly registered** with all ECO partner portals
2. **Download GSTR-2A** and check for TCS entries from each ECO (after 10th of month)
3. **Navigate to TDS/TCS Credit Received** section on GST portal; accept verified credits before GSTR-3B filing
4. **For Agoda:** Review commission basis — is commission being charged on the GST amount? Document all instances
5. **For TravelStack:** Confirm business model in writing — Agency or Merchant?
6. **GSTR-1 Table 14:** Start reporting ECO-wise supplies in GSTR-1 from the month this was applicable (January 2024)

---

## Key Legal Provisions Quick Reference

| Provision | Reference | Content |
|----------|-----------|---------|
| TCS obligation | Section 52, CGST Act | ECOs must collect TCS on net value of supplies |
| TCS rate (current) | CBIC Notification 15/2024 | 0.5% (0.25% CGST + 0.25% SGST or 0.5% IGST) |
| TCS rate (historical until Jul 9, 2024) | Section 52 original | 1% (0.5% CGST + 0.5% SGST or 1% IGST) |
| ECO as deemed supplier | Section 9(5), CGST Act | ECO pays GST (not TCS) for unregistered suppliers in accommodation, taxi, housekeeping |
| GSTR-8 filing obligation | Rule 67, CGST Rules | Monthly by 10th of next month |
| Annual statement | Section 52(10) | GSTR-9B by December 31 |
| New GSTR-1 Table 14/15 | GSTN advisory Jan 2024 | Supplier reports ECO-wise supplies; ECO reports Sec 9(5) supplies |

---

## Created Skill

A dedicated skill for future use has been created at:  
`/home/linux_wsl/Staybird/MMT/.agents/skills/gst-tcs-reconciliation/`

Activate by mentioning: "TCS reconciliation", "GSTR-8 mismatch", "OTA TCS", "ECO TCS credit"
