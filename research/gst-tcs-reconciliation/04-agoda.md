# Agoda Company Pte. Ltd. — GST TCS Profile & Reconciliation

**Company:** Agoda Company Pte. Ltd.  
**Incorporation:** Singapore (Private Company)  
**Indian PAN:** AAQCA5807N  
**Parent:** Booking Holdings (formerly Priceline Group, NASDAQ: BKNG)  
**Indian Registration Type:** Foreign Company / Non-Resident Taxable Person Category with ECO status

---

## 1. GST Registration Details

Agoda Company Pte. Ltd. registered as a **foreign entity** under Indian GST with Tax Collector (ECO) status across multiple states.

### Key ECO GSTINs Identified:

| State | GSTIN | Registration Date | Status |
|-------|-------|-----------------|--------|
| Multiple states | 16AAQCA5807N1CG | March 19, 2021 | Active – Tax Collector ECO |
| Gujarat | 24AAQCA5807N1CJ | 2021 | Active – Tax Collector ECO |
| Goa | 30AAQCA5807N1CQ | March 16, 2021 | Active |
| Rajasthan | 08AAQCA5807N1CD | 2021 | Active – Tax Collector ECO |

> **Note on Coverage:** GSTIN 16AAQCA5807N1CG appears to indicate registration across 36 Indian states per some sources. However, under Indian GST law, a foreign company typically needs **separate state-level GSTINs** for each state where it operates as an ECO.

### Separate Entity — Agoda International India Private Limited

There is also an Indian subsidiary:
- **Company:** AGODA INTERNATIONAL INDIA PRIVATE LIMITED
- **PAN:** AAKCA7646M
- **GSTIN (Maharashtra):** 27AAKCA7646M1Z1
- This entity handles Agoda's Indian office operations, NOT the ECO TCS function

> **For reconciliation:** TCS credits will appear under **Agoda Company Pte. Ltd. (AAQCA5807N)** GSTINs, NOT under the Indian subsidiary GSTIN.

---

## 2. Agoda's GST Compliance History and Issues

### FHRAI Complaint Against Agoda (Active Dispute)

The Federation of Hotel & Restaurant Associations of India (FHRAI) filed a formal complaint against Agoda regarding non-compliance with Indian GST regulations:

**Allegation 1: Commission Charged on GST Amount**
- Agoda introduced a pricing model called **"Reference Sell Rate" (RSR)**
- This model calculates commission on the **total room rate including GST** (not on the pre-tax amount)
- This is allegedly **prohibited under Indian taxation laws** (commission should only be on taxable value, not on the tax component)
- **Impact on Reconciliation:** If Agoda is charging commission on GST, the NET payout to the hotel is lower than it should be, creating a discrepancy between gross bookings, TCS amounts, and actual receipts

**Allegation 2: GST Not Charged on Agoda's Commission Invoices**
- Agoda allegedly does NOT charge GST on its own commission invoices issued to Indian hotels
- This shifts the tax burden to hotels and creates GST reconciliation complications
- Indian hotels cannot claim ITC on commission paid to Agoda if Agoda does not issue valid GST-compliant invoices

**Allegation 3: Non-Transparent Accounting**
- Agoda's accounting practices for settlements are alleged to be non-transparent
- Hotels face difficulty reconciling the actual settlement amount with their booking records

---

## 3. Unique Features of Agoda's GST Reporting

### 3.1 Foreign Company Complications
As a Singapore-based company, Agoda's Indian GST compliance involves:
- **Appointment of an authorized signatory in India** (required for GSTIN)
- **Advance tax deposit** at time of registration (NRTP requirement)
- **No Indian PAN-linked GSTR-9** (annual return complexities differ from Indian companies)

### 3.2 TCS Application Method
Agoda operates on a **closed/opaque pricing model** where:
- Hotels provide a **net rate** to Agoda (lower than retail) 
- Agoda **marks up** and sells to consumer
- The TCS base should be the **amount Agoda collects on behalf of the hotel** (i.e., the hotel's net rate), NOT Agoda's retail selling price

**Reconciliation Challenge:** Because Agoda's retail price to consumers is not always transparent to hotels, verifying the TCS base is difficult. The TCS in GSTR-8 should reflect the amount Agoda collected ON BEHALF of the hotel as a supplier.

### 3.3 Merchant vs. Agency Model
Agoda's pricing model (RSR — Reference Sell Rate) suggests it may be acting more as a **merchant/principal** in some transactions rather than a pure agent. If Agoda is the principal:
- TCS rules under Section 52 do NOT apply (TCS only applies to supplies by OTHER suppliers through the ECO)
- Agoda would pay GST on its own supply instead
- Hotel gets payment as a B2B sale to Agoda

**Impact on your books:** If Agoda acts as merchant, your GSTR-1 shows Agoda as the customer (B2B invoice to Agoda), not a direct consumer sale. No TCS credit should be expected.

---

## 4. How to Identify TCS from Agoda in GSTR-2A

**Step 1:** Go to GST Portal → View GSTR-2A → Filter by ECO/TCS entries

**Step 2:** Look for GSTIN starting with the PAN **AAQCA5807N** (Agoda Company Pte. Ltd.)

**Step 3:** Cross-reference with your state:
- If hotel is in Goa → Look for 30AAQCA5807N1CQ
- If hotel is in Rajasthan → Look for 08AAQCA5807N1CD
- If hotel is in Gujarat → Look for 24AAQCA5807N1CJ

**Step 4:** Compare the taxable value shown in Agoda's GSTR-8 with your internal booking records for Agoda channel.

---

## 5. Reconciliation Challenges — Transaction-Level

### 5.1 Net Rate vs. Retail Rate Mismatch
If Agoda has adopted the merchant model:
- No TCS appears in your GSTR-2A
- Your sale is to Agoda (B2B invoice required)
- Revenue recognition in books: Net rate received from Agoda

If Agoda is acting as agent:
- TCS appears in GSTR-2A
- Your revenue: Full selling price (gross) 
- Agoda's commission is your input service

**Action:** Confirm contractual model with Agoda account manager and get written confirmation of whether GSTR-8 TCS is being filed against your GSTIN.

### 5.2 Commission on GST Issue — Practical Impact
If Agoda charges commission on the GST amount:
- Your net payout is REDUCED by an extra X% of your GST amount
- But the TCS is computed on the pre-GST taxable value
- This creates a **phantom settlement shortfall** that is NOT a GST issue per se, but affects your P&L reconciliation

### 5.3 Cancellations and Refunds
Agoda's cancellation policy (often free cancellation until a day before check-in) means significant volumes of cancellations. For TCS:
- Cancellations in the same month are netted in GSTR-8 for that month
- Cancellations in subsequent months adjust the NEXT month's GSTR-8

---

## 6. Key Reconciliation Actions for Agoda

1. **Clarify business model:** Agent vs. Merchant — get it in writing from Agoda
2. **Review property statements:** Monthly download from Agoda Extranet (ycs.agoda.com)
3. **Check GSTR-2A monthly:** Look for Agoda's PAN-linked GSTINs
4. **Raise FHRAI complaint support:** If commission is being charged on GST amount, document the discrepancy and check if FHRAI bulletins apply
5. **Commission invoice review:** Request GST-compliant commission invoices from Agoda (with GSTIN, GST charged, and basis of calculation on PRE-TAX room rate only)

---

## 7. Practical Monthly Reconciliation Steps

| Step | Action | Data Source |
|------|--------|------------|
| 1 | Download Agoda booking report for month | Agoda Extranet / Ycs.agoda.com |
| 2 | Calculate net bookings (after cancellations) | Internal |
| 3 | Check GSTR-2A for Agoda ECO GSTIN entries | GST Portal (after 11th) |
| 4 | If no TCS in GSTR-2A, verify business model | Agoda Contract |
| 5 | If TCS amount mismatches, raise with Agoda | Agoda Account Manager |
| 6 | Check commission invoice for GST compliance | Payment Statement |
| 7 | Document RSR/commission-on-GST issues separately | Compliance file |
