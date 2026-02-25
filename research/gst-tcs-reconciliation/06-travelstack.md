# TravelStack Tech Limited — GST TCS Profile & Reconciliation

**Company:** TravelStack Tech Limited  
**Type:** Public Limited Company (India)  
**PAN:** AAFCC6416Q  
**Business Activity:** Tour operator services, reservation services for accommodation and package tours

---

## 1. Background — Who is TravelStack?

TravelStack Tech Limited (formerly known as Cox & Kings Financial Services or related entity — to be verified) is an Indian travel technology company that operates as an Online Travel Agency (OTA) and tour platform. It provides:
- Tour operator services
- Hotel and accommodation reservations
- Package tour reservations through digital platform

Given these activities, TravelStack qualifies as an **Electronic Commerce Operator (ECO)** under GST law.

> **Research Note:** TravelStack Tech Limited appears to be less prominently documented as an OTA compared to MakeMyTrip, Yatra, or Cleartrip. It may be a B2B/corporate travel facilitator or a white-label OTA platform. Verify exact business model with your account manager at TravelStack.

---

## 2. GST Registration Details

TravelStack Tech Limited has multiple state GSTINs:

### Identified GSTINs:

| State | GSTIN | Registration Date | Type |
|-------|-------|-----------------|------|
| West Bengal | 19AAFCC6416Q1Z3 | July 4, 2017 | Service Provider / Regular |
| Maharashtra | 27AAFCC6416Q1Z6 | June 29, 2017 | Regular |
| Himachal Pradesh | 02AAFCC6416Q1ZI | September 1, 2018 | Regular |
| Andhra Pradesh | 37AAFCC6416Q1Z5 | July 6, 2017 | Regular |
| Uttar Pradesh | 09AAFCC6416Q1Z4 | June 29, 2017 | Regular |

> **Important Observation:** The GSTINs identified for TravelStack Tech Limited appear to be **regular taxpayer GSTINs** (14th character 'Z'), NOT Tax Collector ECO GSTINs (14th character 'C'). This is a critical distinction.

---

## 3. Two Possible Interpretations for Reconciliation

### Scenario A: TravelStack is a Regular Service Provider (NOT an ECO)

If TravelStack Tech Limited is itself a service provider (e.g., an offline tour operator that has a tech platform for its OWN bookings), then:
- TravelStack is NOT an ECO
- TravelStack does NOT collect TCS
- **No TCS credit will appear in your GSTR-2A from TravelStack**
- Instead, you may receive B2B invoices from TravelStack for room/accommodation, and you should raise B2B invoices TO TravelStack or TO customers directly

### Scenario B: TravelStack acts as Platform/Aggregator ECO

If TravelStack operates a platform through which third-party hotel suppliers offer accommodation, and TravelStack collects consideration from end customers, then:
- TravelStack would need to register as ECO Tax Collector
- Look for TCS GSTINs with 'C' as 14th character under PAN AAFCC6416Q
- TCS credit would appear in your GSTR-2A

**Action Required:** Contact TravelStack's finance team to confirm:
1. Does TravelStack collect consideration from end customers on your behalf?
2. Are they registered as Tax Collector ECO?
3. What is their ECO GSTIN (if applicable)?

---

## 4. Red Flags for No-TCS from TravelStack

If TravelStack does NOT file GSTR-8 against your GSTIN but you are receiving bookings and payments through them, investigate:

**Red Flag 1:** All GSTINs end in 'Z' (regular taxpayer), none end in 'C' (ECO)  
→ Likely NOT an ECO; they are a regular tour operator buying your services

**Red Flag 2:** You receive NET payment from TravelStack without TCS deduction mentioned  
→ TravelStack may be buying accommodation at net rate (merchant model) → You raise B2B invoice to TravelStack

**Red Flag 3:** TravelStack raises commission invoices TO YOU (not from you to them)  
→ This is a net rate / merchant model; TCS does NOT apply; you report gross revenue in GSTR-1 with TravelStack as customer

---

## 5. How to Determine TCS Obligation from TravelStack

### Decision Tree:

```
Does TravelStack collect payment from end customer on your behalf?
├── YES → Is TravelStack registered as Tax Collector ECO?
│         ├── YES → TCS applies → Look for TCS in GSTR-2A
│         └── NO → Non-compliant; approach TravelStack for ECO registration evidence
└── NO → TravelStack buys your service at net rate → 
         You raise B2B invoice to TravelStack → TCS NOT applicable to you
```

---

## 6. Common Business Model with Smaller OTAs (Like TravelStack)

Smaller OTAs often use **Net Rate / Merchant Model** to avoid ECO compliance complexity:
- Hotel provides a **contracted net rate** (e.g., ₹5,000 per room)
- OTA sells to consumer at higher price (e.g., ₹7,000) and keeps the margin (₹2,000)
- Hotel raises invoice to OTA for ₹5,000 + GST
- OTA pays full invoice to hotel

Under this model:
- TCS is NOT applicable to the hotel
- Hotel reports the ₹5,000 as B2B sale in GSTR-1 with OTA as customer
- No TCS credit in GSTR-2A

This model is simpler for compliance reasons and is commonly adopted by smaller OTAs.

---

## 7. Reconciliation Framework for TravelStack

### If Agency Model (TCS Applicable):

| Item | Data Source |
|------|------------|
| Bookings collected by TravelStack | TravelStack partner portal statements |
| Cancellations (same month) | TravelStack statements |
| Net value per books | Internal records |
| GSTR-8 Net value | GSTR-2A (filtered by AAFCC6416Q GSTINs) |
| Expected TCS | Net value × 0.5% |
| Received TCS credit | GSTR-2A |

### If Merchant/Net Rate Model (No TCS):

| Item | Data Source |
|------|------------|
| TravelStack invoices payable to you | B2B invoices raised by you |
| Revenue recognized | Contracted net rate |
| GST charged on invoices | Your invoice to TravelStack |
| ITC claimed by TravelStack | Their compliance (separate) |
| Your GSTR-1 | Report TravelStack as customer in B2B supplies |

---

## 8. Action Items for TravelStack TCS Status

1. **Request written confirmation** from TravelStack: Are they registered as Tax Collector ECO?
2. **Ask for their ECO GSTIN** (should end in 'C')
3. **Check your GSTR-2A** for entries from any AAFCC6416Q GSTINs
4. **Review your contract:** Does it specify "TCS deducted by TravelStack" or "Net rate settlement"?
5. **Obtain TravelStack's monthly settlement statement** — check if TCS line item appears
6. **Verify source of payment:** Does TravelStack pay you the full room rate + GST (then charge commission separately), or net payout?

---

## 9. If TravelStack Should be Collecting TCS But Is Not

If you determine TravelStack is acting as an ECO but NOT filing GSTR-8:
- This is a **compliance failure** by TravelStack
- Under GST law, if TCS is not collected and deposited, the government may recover the TCS amount **from the ECO** (not from you)
- However, the matching credit in your Electronic Cash Ledger will also be absent
- **Action:** Issue a formal legal notice to TravelStack demanding GSTIN details and GSTR-8 filing evidence. Document the correspondence for audit trail.
