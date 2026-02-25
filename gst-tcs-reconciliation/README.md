# GST TCS Reconciliation — README

## Overview

This skill provides expert guidance for hotels, tour operators, and other service providers who receive bookings through Online Travel Agencies (OTAs) and need to reconcile GST Tax Collected at Source (TCS) with their books of accounts.

## Supported ECOs

| E-Commerce Operator | PAN | Research File |
|---------------------|-----|---------------|
| MakeMyTrip (India) Pvt. Ltd. | AADCM5146R | `/research/gst-tcs-reconciliation/01-makemytrip.md` |
| Cleartrip Private Limited | AACCC6016B | `/research/gst-tcs-reconciliation/02-cleartrip.md` |
| Airbnb Payments India Pvt. Ltd. | AANCA6203B | `/research/gst-tcs-reconciliation/03-airbnb.md` |
| Agoda Company Pte. Ltd. | AAQCA5807N | `/research/gst-tcs-reconciliation/04-agoda.md` |
| Yatra Online Limited | AAACY2602D | `/research/gst-tcs-reconciliation/05-yatra.md` |
| TravelStack Tech Limited | AAFCC6416Q | `/research/gst-tcs-reconciliation/06-travelstack.md` |

## Installation

This skill is located at: `.agents/skills/gst-tcs-reconciliation/`

## Quick Start

1. **Identify the ECO** causing the reconciliation issue
2. **Read the ECO-specific research file** (links above)
3. **Use the master reconciliation guide**: `/research/gst-tcs-reconciliation/07-comprehensive-reconciliation.md`
4. **Look up GSTINs**: `references/eco-gstin-directory.md`

## Key Legal Reference

- **Section 52, CGST Act, 2017** — TCS obligation for ECOs
- **CBIC Notification 15/2024** — TCS rate reduced from 1% to 0.5% effective July 10, 2024
- **GSTR-1 Table 14 / Table 15** — New reporting requirements from January 2024

## Trigger Phrases

This skill is activated when the user mentions:
- "TCS reconciliation"
- "GSTR-8 reconciliation"  
- "TCS from MakeMyTrip / Cleartrip / Airbnb / Yatra / Agoda / TravelStack"
- "Tax collected at source OTA"
- "GSTR-2A TCS credit"
- "ECO TCS mismatch"
- "GST TCS hotel OTA"
