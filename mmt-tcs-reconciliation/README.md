# MakeMyTrip (MMT) TCS Reconciliation Skill

Provides automated reconciliation of GST Tax Collected at Source (TCS) reported by MakeMyTrip (India) Pvt. Ltd. (collector GSTIN `27AADCM5146R1C6`) against the primary Earnings Reports downloaded from the MMT extranet.

## Rationale
GST Section 52 mandates TCS collection on the "net value of taxable supplies made." For hotel properties, a supply is legally "made" during the guest's check-in / stay, not when the booking is originally placed. Extensive data analysis confirms that MakeMyTrip correctly tracks and reports TCS to the GST portal tied to the **Check-in Date**, matching the *Earnings Reports*, rather than the Booking Reports.

## Included Components
- **`scripts/reconcile_mmt_tcs.py`**
  Automated Python script that takes all MMT `.csv` files inside an `EarningsReport/` folder, filters by "Checkin Date", sorts out cancelled versus confirmed reservations for all MMT-affiliated brands, and produces an actionable variance summary. 

## Requirements
To successfully use this skill:
1. Access the MMT Net Earnings Extranet specifically at:
   [https://in.goibibo.com/newextranet/payments/net-earnings](https://in.goibibo.com/newextranet/payments/net-earnings)
2. Generate and download "Net Earnings" reports containing the fields `Property Gross Charges`, `TCS Amount`, `Checkin Date`, and `Brand`.
3. Save the `.csv` dumps to the designated `EarningsReport` directory within your workspace.

## Usage
Simply trigger the reconciliation script. The agent will read all the properties' CSVs and compare the sum to the GST portal figures. Any discrepancies (such as bookings crossing into new months) will be itemized to confidently file your GSTR-8 (TDS and TCS Credit Received) claims.
