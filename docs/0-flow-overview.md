# Base Flow Overview

On Interact, we follow a standard process for all products, with minor deviations (shown below).  

| Step                | Role                  | Actions                                                                                   | Notes                                                                                                      |
|---------------------|-----------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **Refer**           | Claimant              | Upload evidence and capture/update positions.                                             | First step of the flow.                                                                                    |
| **Respond**         | Defendant             | Review claim, optionally upload evidence, capture/update positions.                       | Defendant can **Accept & Settle** at this stage, publishing a binding Settlement Agreement.                |
| **Final Review**    | Claimant              | Review Defendant’s response. Optionally reject if Defendant uploaded additional evidence. | Applies in OIC and Credit Hire (always has Final Review). <br> **MoJ is two-step only** (no Final Review). |
| **Accept & Settle** | Defendant or Claimant | Accept the claim as it stands, without countering.                                        | Publishes a Settlement Agreement and ends the process. Binding like an arbitral award.                     |
| **Arbitration**     | Arbitrator            | Arbitrator decides the case on the papers and issues an award with reasons and costs.     | Product-dependent. Limited correction window applies.                                                      |

!!! Note
    If the Defendant chooses to reject the claim upon receipt of the referral, a certificate of case status is published to the case record which the claimant may use in court as evidence of their attempt to arbitrate. This certificate contains the defendant's response and rejection reasons.


### Product differences (vs Base)

| Item / Step                                      | OIC       | MoJ     | CHC       |
|--------------------------------------------------|-----------|---------|-----------|
| **Refer (Claimant refers claim)**                | Yes       | Yes     | Yes       |
| **Respond (Defendant responds)**                 | Yes       | Yes     | Yes       |
| **Final Review (Claimant)**                      | **Yes**   | **No**  | **Yes**   |
| **Accept & Settle at Respond (Defendant)**       | Yes       | Yes     | Yes       |
| **Accept & Settle at Final Review (Claimant)**   | **Yes**   | **No**  | **Yes**   |
| **Final‑Review: Reject for Additional Evidence** | **Yes**\* | **No**  | **Yes**\* |
| **Arbitration**                                  | Yes       | Yes     | Yes       |
| **Neutral nomination (Admin)**                   | Yes†      | Yes†    | Yes†      |
| **Award correction window**                      | Limited   | Limited | Limited   |

!!! info
    \* Available only when the Defendant uploaded at least one document tagged **Additional evidence** during **Respond**.
    † Neutral (arbitrator) is nominated by Admin per current protocols.

---

!!! note "Legend & Notes"
    **Yes / No** indicates whether the capability/step is present in the product.
    **Additional evidence condition** — the claimant’s **Reject** at Final Review is available **only** if the Defendant uploaded **Additional evidence** in the Respond step.

---

### Documents by Step: Required vs Optional

| Step / Touchpoint                            | OIC                                                                 | MoJ                                                                                                  | CHC                                        |
|----------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------|
| **1. Upload Supporting Evidence (Claimant)** | **Req:** OIC document list & docs<br>**Opt:** Additional evidence     | **Req:** Court Proceedings Pack (Part A only); Part B Offer<br>**Opt:** Interest calculation; medical records served; documentary evidence served | **Req:** Evidence<br>**Opt:** Pre‑arb offer |
| **2. Respond (Defendant)**                   | **Req:** —<br>**Opt:** Additional evidence; submissions; final offer  | **Req:** —<br>**Opt:** —                                                                                | **Req:** Evidence<br>**Opt:** Submissions; pre‑arb offer |
| **3. Final Review (Claimant)**               | **Req:** —<br>**Opt:** Submissions                                   | **Req:** N/A<br>**Opt:** N/A                                                                           | **Req:** —<br>**Opt:** Submissions         |

!!! info
    **Legend:** `—` = nothing standard/required; `N/A` = step not present in this product.

---
