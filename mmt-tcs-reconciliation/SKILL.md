---
name: mmt-tcs-reconciliation
description: "Reconciles GST TCS (Tax Collected at Source) data from MakeMyTrip (MMT) with Earnings Reports downloaded from the MMT extranet based on check-in dates."
version: 1.0.0
author: Staybird
created: 2026-02-25
platforms: [claude-code]
category: data-analysis
tags: [gst, tcs, makemytrip, mmt, reconciliation, finance]
risk: safe
---

# MMT TCS Reconciliation Skill

## Purpose
Automates the reconciliation of GST Tax Collected at Source (TCS) reported by MakeMyTrip (India) Pvt. Ltd. (MMT) in their GSTR-8 portal filings against the actual booking data. Based on deep discrepancy analysis, this skill correctly identifies that MMT tracks GST TCS liability based on the **checkout month (tied to Check-in date filtering)** and uses the **Earnings Report** (not the Booking Report) as the source of truth for the most accurate reconciliation.

## When to Use This Skill
This skill should be used when:
- Reconciling monthly GST TCS amounts collected by MakeMyTrip/Goibibo.
- Investigating discrepancies between the GST Portal Gross Value and the hotel's extranet records.
- Verifying whether to accept or reject the auto-populated TCS credit on the GST Portal.
- Generating final reconciliation summaries for accounting and GSTR-1 Table 14(a) reporting.

## Core Capabilities
- **Automated Earnings Parsing:** Reads 'Net Earnings' CSV reports downloaded from the MMT extranet.
- **Precise Data Filtering:** Filters data strictly based on the **Check-in Date** column to perfectly align with MMT's GSTR-8 filing logic (Scenario A).
- **TCS and Gross Summary Generation:** Calculates total net gross revenue and total expected TCS across all properties and MMT sub-brands (MakeMyTrip, Goibibo, etc.).
- **Variance Analysis:** Highlights structural timing differences (e.g., month-crossing stays, out-of-period cancellations) that typically explain innocuous gross value variances.

## Process Workflow

### 1. Data Download
Download the relevant month's Earnings Reports for all properties.
- **Reference link:** [Download Net Earnings Reports from MMT Extranet](https://in.goibibo.com/newextranet/payments/net-earnings)
- Export the data as CSV files and place them in the project workspace (e.g., `EarningsReport/` directory).

### 2. Execution
Run the provided reconciliation script over the downloaded CSV files:
```bash
python scripts/reconcile_mmt_tcs.py
```
*Note: Ensure the script parameters or constants are configured for the correct month/year.*

### 3. Verification & Action
- **TCS Amount Matching:** If the calculated Neto TCS matches the GST portal's Total TCS within a small rounding tolerance (e.g., ₹100), the figure is considered fully reconciled.
- **Action:** Accept the TCS credit on the GST Portal (Services → Returns → TDS and TCS Credit Received).
- **Gross Value Variances:** It is standard to observe gross value mismatches due to multi-night stays crossing month boundaries or cancellation adjustment timings. As long as the calculated TCS matches, you can confidently accept the portal credits.

## Bundled Resources
- **Reconciliation Script:** `scripts/reconcile_mmt_tcs.py` automates the extraction and reconciliation logic based on check-in dates.
