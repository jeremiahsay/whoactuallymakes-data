# Who Actually Makes: open data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23920936.svg)](https://doi.org/10.5281/zenodo.23920936)

Who makes store-brand products, from public records. Every list behind [Who Actually Makes](https://whoactuallymakes.com/): which company each Kirkland Signature product traces to, the companies behind store brands and the labels they're on record for, every NHTSA tire plant code, what tire makers and carmakers say about tire age, and the evidence, sources, corrections and update schedule behind it all.

**9 datasets · 1,637 records · version 2026-11-03** · JSON and CSV (UTF-8) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Live copy and API: https://whoactuallymakes.com/data/

Each answer on the site carries a stamp (confirmed, documented, reported or unverified) and links to the record it rests on. The evidence file keeps the exact quote, the date it was read and a SHA-256 fingerprint of the document, so anyone can check a row against its source. How the stamps work: https://whoactuallymakes.com/how-we-know/

## Datasets

| Dataset | Records | Updated | Files | On the site |
|---|---:|---|---|---|
| [Who makes what: store-brand answers (Kirkland Signature)](#claims) | 44 | 2026-11-03 | [JSON](data/claims.json) (41 KB) · [CSV](data/claims.csv) (26 KB) | [/kirkland-signature/](https://whoactuallymakes.com/kirkland-signature/) |
| [Companies behind store brands (maker pages)](#companies) | 7 | 2026-11-03 | [JSON](data/companies.json) (4 KB) · [CSV](data/companies.csv) (2 KB) | [/makers/](https://whoactuallymakes.com/makers/) |
| [Which store labels each company is on record for](#company-labels) | 128 | 2026-11-03 | [JSON](data/company-labels.json) (65 KB) · [CSV](data/company-labels.csv) (40 KB) | [/makers/](https://whoactuallymakes.com/makers/) |
| [Tire plant codes (NHTSA)](#tire-plants) | 1,246 | 2026-11-02 | [JSON](data/tire-plants.json) (149 KB) · [CSV](data/tire-plants.csv) (89 KB) | [/tire-dot-code-lookup/](https://whoactuallymakes.com/tire-dot-code-lookup/) |
| [Tire age guidance from tire makers, carmakers and agencies](#tire-age) | 22 | 2026-11-03 | [JSON](data/tire-age.json) (34 KB) · [CSV](data/tire-age.csv) (19 KB) | [/tire-date-code/](https://whoactuallymakes.com/tire-date-code/) |
| [Evidence records: every quote behind our answers](#evidence) | 135 | 2026-11-03 | [JSON](data/evidence.json) (117 KB) · [CSV](data/evidence.csv) (91 KB) | [/how-we-know/](https://whoactuallymakes.com/how-we-know/) |
| [Sources: the public records we use, and their limits](#sources) | 45 | 2026-11-03 | [JSON](data/sources.json) (49 KB) · [CSV](data/sources.csv) (25 KB) | [/sources/](https://whoactuallymakes.com/sources/) |
| [Corrections log](#corrections) | 4 | 2026-11-03 | [JSON](data/corrections.json) (4 KB) · [CSV](data/corrections.csv) (3 KB) | [/corrections/](https://whoactuallymakes.com/corrections/) |
| [Update schedule: when each list is checked](#schedule) | 6 | 2026-11-03 | [JSON](data/schedule.json) (25 KB) · [CSV](data/schedule.csv) (1 KB) | [/update-schedule/](https://whoactuallymakes.com/update-schedule/) |

<a id="claims"></a>

### Who makes what: store-brand answers (Kirkland Signature)

Every store-brand product we can answer from a public record, one row per company the record names: the product, the company, what the record says it did (made, bottled, imported, recalled), the stamp, the dates and lots it covers, the words to look for on the label, and links to the records.

- **Limits:** Each row covers only its own dates, lots and region. A label approval names the bottler or importer, not always the distiller; a recall names the recalling firm, usually but not always the maker.
- **Kept fresh:** Whenever a claim is added or re-checked; every claim is re-checked within 6 months
- **Rights:** Quoted words belong to their publishers; most records are US government work. CC BY covers our rows.
- **Files:** `data/claims.json`, `data/claims.csv` · live: https://whoactuallymakes.com/data/claims.json

<details><summary>The 19 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `claim_id` | text | Our ID for the claim. Stable. |
| `brand` | text | The store brand. |
| `product` | text | The product, as we name it. |
| `category` | text | Product category. |
| `company` | text | The company the record names. |
| `company_legal_name` | text | Its name as the record gives it. |
| `relation` | text | made-by, bottled-by, packed-by, imported-by or recalled-by. |
| `stamp` | text | confirmed, documented, reported or unverified (see /how-we-know/). |
| `from` | date | Start of what the record covers (YYYY-MM or YYYY-MM-DD). |
| `to` | date | End of what it covers; blank when open-ended. |
| `region` | text | Where the record applies. |
| `variant` | text | Which versions of the product, if the record says. |
| `on_label` | text | Words to look for on the pack, from the record. |
| `summary` | text | One sentence on what the evidence shows. |
| `evidence_ids` | text | IDs of the evidence records, separated by “ \| ”. |
| `evidence_urls` | url | Links to those records, same order. |
| `last_checked` | date | When we last checked the claim against its records. |
| `next_check` | date | When it’s next due. |
| `page` | url | Our answer page, if there is one. |

</details>

<a id="companies"></a>

### Companies behind store brands (maker pages)

One row per company page: the company, its legal names, what it makes, how many Kirkland Signature claims and products we tie to it, how many other companies a state pet food register lists in its care, how many FDA recalls it has and how many store names those recalls print, and its page.

- **Limits:** Counts are as of the read date. A company with no page yet isn't here; the claims file names every company we have a record for.
- **Kept fresh:** Whenever a claim, register or recall read changes; registers are re-read every 6 months
- **Rights:** Most counts come from US government records. CC BY covers our rows.
- **Based on:** 3 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/companies.json`, `data/companies.csv` · live: https://whoactuallymakes.com/data/companies.json

<details><summary>The 15 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `company_slug` | text | Our ID for the company page. Stable. |
| `company` | text | The company, as its page names it. |
| `legal_names` | text | Legal names of the company and its group companies on the page, separated by “ \| ”. |
| `website` | url | The company’s own website. |
| `category` | text | What it mainly makes. |
| `about` | text | One line on the company, from its own statements and the records. |
| `kirkland_claims` | number | Kirkland Signature claims that name it (see the claims file). |
| `kirkland_products` | number | Distinct Kirkland Signature products in those claims. |
| `register_other_companies` | number | Other companies with live registrations in its care on North Dakota’s pet food register; blank if we didn’t read the register for it. |
| `fda_recalls` | number | FDA enforcement reports (recalls) naming it as the recalling firm; blank if we didn’t read them. |
| `fda_recall_store_names` | number | Store names printed in the product text of those recalls. |
| `plants` | number | Plants listed on its page, each from a source. |
| `page` | url | Our company page. |
| `last_checked` | date | Latest check of anything on the page. |
| `next_check` | date | When the earliest claim on the page is next due. |

</details>

<a id="company-labels"></a>

### Which store labels each company is on record for

One row per link between a company and a brand or retailer: a claim on our answer pages, a registration on North Dakota’s pet food register filed in the company’s care, a store name printed in the company’s FDA recalls, or a brand listed under the company’s API engine oil license. Each row says how many records back it, the dates they cover, and links the record.

- **Limits:** A register row shows the company is the registered contact for those products, not that it made each one. A recall row shows the store name was printed in the recall’s product text; it doesn’t prove a current supply deal. Rows cover only their own dates. An API license row shows the company answers to API for that brand’s oils, not which plant blended them or who owns the brand.
- **Kept fresh:** Whenever a claim, register or recall read changes; registers are re-read every 6 months
- **Rights:** Most records are US government work. CC BY covers our rows.
- **Based on:** 3 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/company-labels.json`, `data/company-labels.csv` · live: https://whoactuallymakes.com/data/company-labels.json

<details><summary>The 11 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `company_slug` | text | The company page this row is on (see the companies file). |
| `company` | text | The company. For claim rows, the one the record names, which can be a group company. |
| `label` | text | The store brand or retailer, as we name it. |
| `link_kind` | text | claim, state-pet-food-register, fda-recall or api-oil-license. |
| `detail` | text | For a claim, what the record says and the product; for a register row, the registrant name as filed; for a recall row, what the link means; for a license row, the brand names exactly as API lists them. |
| `count` | number | Claims (1), live registrations (0 = only lapsed ones), recalls that print the store name, or oils listed under the license. |
| `first` | date | Earliest date the records cover; blank if they don’t say. |
| `last` | date | Latest date they cover. For a register row, the latest expiry of a live registration; for a license row, when the license expires. |
| `record_url` | url | The record: claim evidence (separated by “ \| ”), the register listing, or the latest recall. |
| `read_on` | date | When we read the record. |
| `company_page` | url | Our company page. |

</details>

<a id="tire-plants"></a>

### Tire plant codes (NHTSA)

Every plant code NHTSA has assigned to a tire factory: the code from the start of a tire’s DOT number, the factory’s name, city, state or province, country and whether it is active.

- **Limits:** A plant code shows which factory made a tire, not which brand sold it. Status is as NHTSA lists it; closed plants keep their codes.
- **Kept fresh:** Weekly, by script, from NHTSA’s vPIC list
- **Rights:** The codes and factory details are US government work (NHTSA), in the public domain in the US. CC BY covers our compiled file.
- **Based on:** 2 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/tire-plants.json`, `data/tire-plants.csv` · live: https://whoactuallymakes.com/data/tire-plants.json

<details><summary>The 7 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `code` | text | The plant code: the 2 or 3 characters after “DOT” on a tire. |
| `old_code` | text | The older 2-character code for the same plant, if NHTSA lists one. |
| `name` | text | The factory or company name as NHTSA lists it. |
| `city` | text | City of the factory. |
| `state` | text | State, province or region of the factory. |
| `country` | text | Country of the factory. |
| `status` | text | Active, Closed, or blank when NHTSA gives no status. |

</details>

<a id="tire-age"></a>

### Tire age guidance from tire makers, carmakers and agencies

What each tire maker, carmaker and safety agency says about replacing tires by age, in a row per maker: the age, what it’s counted from, whether it covers the spare, and the document it comes from.

- **Limits:** Each row speaks only for the maker’s own tires, or for the vehicle model and year named. It is advice, not law, except the UK row, which describes a legal ban on tires over 10 years old for some heavy vehicles.
- **Kept fresh:** Re-read by hand every year, and whenever a maker changes its advice
- **Rights:** Quoted words in the source columns belong to their publishers; we quote them so you can check each row. CC BY covers our rows and wording.
- **Based on:** 24 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/tire-age.json`, `data/tire-age.csv` · live: https://whoactuallymakes.com/data/tire-age.json

<details><summary>The 14 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `group` | text | “tire maker or agency” or “carmaker”. |
| `who` | text | The maker or agency. |
| `covers` | text | What the advice covers: the kind of source, or for carmakers the model, year and market of the manual. |
| `replace_at` | text | The age the maker gives, in its own terms. |
| `years` | number | That age as a number of years, for carmakers; 0 when the manual gives no age. |
| `counted_from` | text | Where the years count from: manufacture (the DOT date code), fitting, or not stated. |
| `spare` | text | Whether the advice covers the spare (carmakers). |
| `also` | text | Other conditions the maker attaches (tire makers and agencies). |
| `summary` | text | One plain sentence on the carmaker’s advice. |
| `source_titles` | text | Title of each document, separated by “ \| ”. |
| `source_urls` | url | Link to each document, in the same order. |
| `archive_urls` | url | Internet Archive copy of each document, where we used one, in the same order. |
| `quotes` | text | The exact words from each document, in the same order. |
| `read_on` | date | The date we last read the documents (YYYY-MM-DD). |

</details>

<a id="evidence"></a>

### Evidence records: every quote behind our answers

Every document we rely on, one row each: the exact quote, the link, the date we read it, an Internet Archive copy where we used one, and the SHA-256 fingerprint of the file as we read it.

- **Limits:** A record shows what a document said when we read it. Documents change; the fingerprint lets you check whether the one you have is the same.
- **Kept fresh:** Whenever we read or re-read a document
- **Rights:** Quotes belong to their publishers and are short so you can check our work. CC BY covers our records: titles, notes, dates and fingerprints.
- **Based on:** 50 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/evidence.json`, `data/evidence.csv` · live: https://whoactuallymakes.com/data/evidence.json

<details><summary>The 12 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `id` | text | Our ID for the record. Stable: it never changes or gets reused. |
| `source` | text | ID of the source it comes from (see the Sources dataset). |
| `publisher` | text | Who published the document. |
| `type` | text | maker-statement or regulator-document. |
| `title` | text | The document and the section we read. |
| `url` | url | Where the document lives. |
| `archive_url` | url | Internet Archive copy we read or saved, if any. |
| `retrieved` | date | When we read it (YYYY-MM-DD). |
| `doc_date` | date | The date the document gives itself, if it gives one. |
| `quote` | text | The exact words we rely on, up to 600 characters. |
| `sha256` | text | SHA-256 fingerprint of the file as we read it. |
| `note` | text | Page number, how we read it, and anything a checker should know. |

</details>

<a id="sources"></a>

### Sources: the public records we use, and their limits

Each source we use: who publishes it, whether it is a primary record, what it proves, what it can’t prove, what its terms allow, and how and when we read it.

- **Limits:** Describes the sources, not their contents. Terms change; each row carries the date we last checked them.
- **Kept fresh:** Terms re-checked every year; pulls on the schedule shown
- **Rights:** CC BY covers the whole file.
- **Based on:** 45 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/sources.json`, `data/sources.csv` · live: https://whoactuallymakes.com/data/sources.json

<details><summary>The 13 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `id` | text | Our ID for the source. |
| `name` | text | Name of the source. |
| `publisher` | text | Who publishes it. |
| `url` | url | Its home page. |
| `kind` | text | Kind of source, such as Government registry or Maker. |
| `primary` | boolean | true when it is the record itself, not a report about a record. |
| `proves` | text | What it can prove. |
| `cannot_prove` | text | What it can’t prove. |
| `terms_url` | url | Its terms of use or site policies. |
| `terms_read` | text | What its terms allow, in our words. |
| `terms_checked` | date | When we last read its terms. |
| `credit` | text | The credit line the publisher asks for, if any. |
| `pulls` | text | How and how often we read it, separated by “ \| ”. |

</details>

<a id="corrections"></a>

### Corrections log

Every change to a published answer: what it said, what it says now, why, who spotted it and when. Corrections, updates and clarifications are kept apart.

- **Limits:** Starts on Nov 2, 2026, when the site began. An empty log means no answer has changed yet.
- **Kept fresh:** The day a change is made
- **Rights:** CC BY covers the whole file.
- **Files:** `data/corrections.json`, `data/corrections.csv` · live: https://whoactuallymakes.com/data/corrections.json

<details><summary>The 10 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `id` | text | Our ID for the entry. |
| `on` | date | When the change went live (YYYY-MM-DD). |
| `kind` | text | correction, update or clarification. |
| `page` | url | The page that changed (a path on whoactuallymakes.com). |
| `what` | text | What changed, in a few words. |
| `was` | text | What it said before. |
| `now` | text | What it says now. |
| `why` | text | Why it changed. |
| `flagged_by` | text | Who spotted it: a reader, the maker or brand, or our own checks. |
| `evidence` | url | The records that showed it, separated by “ \| ”. |

</details>

<a id="schedule"></a>

### Update schedule: when each list is checked

Each check we run on a schedule: what it reads, how often, by script or by hand, when it last ran, when it’s next due and what it found.

- **Limits:** A job running on time shows we read the source, not that the source was right.
- **Kept fresh:** Every time a job runs
- **Rights:** CC BY covers the whole file.
- **Files:** `data/schedule.json`, `data/schedule.csv` · live: https://whoactuallymakes.com/data/schedule.json

<details><summary>The 9 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `id` | text | Our ID for the job. |
| `what` | text | What the job checks. |
| `source` | text | The source it reads. |
| `how` | text | script or hand. |
| `every_days` | number | How often it runs, in days. |
| `once` | boolean | true for a one-off check. |
| `last` | date | When it last ran (YYYY-MM-DD). |
| `due` | date | When it’s next due (YYYY-MM-DD). |
| `result` | text | What the last run found. |

</details>

## Use it

```python
import pandas as pd
plants = pd.read_csv("https://raw.githubusercontent.com/jeremiahsay/whoactuallymakes-data/main/data/tire-plants.csv")
```

For the always-current copy, read from the site instead: `https://whoactuallymakes.com/data/<dataset>.json`. The catalog (`catalog.json`, also live at /data/catalog.json) lists every file with its size and SHA-256. `datapackage.json` describes the CSVs for Frictionless Data tools.

## Licence and credit

Our rows are licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): free to reuse, commercially too. Credit: **Who Actually Makes (whoactuallymakes.com), CC BY 4.0**, with a link to https://whoactuallymakes.com/data/. Quoted words in the evidence and source columns belong to their publishers. Most records are US government work, in the public domain in the US. See each dataset's Rights line. To cite it, use the DOI https://doi.org/10.5281/zenodo.23920936 (all versions; Zenodo also gives each release its own DOI) or `CITATION.cff` (GitHub's "Cite this repository").

## Corrections

Spotted a wrong row? Tell us at https://whoactuallymakes.com/contact/#wrong. Every change to a published answer is logged in `data/corrections.csv` and at https://whoactuallymakes.com/corrections/.

## About this repository

The site is the source. This repository mirrors it daily by script (`build.py`): each file is checked against the catalog's SHA-256 before it is committed, so the git history is a dated record of every change. Who Actually Makes is published by Numbers Publishing Pte. Ltd., Singapore (https://numbers.sg/company/), and edited by [Jeremiah Say](https://whoactuallymakes.com/about/) ([ORCID](https://orcid.org/0009-0009-2025-7691)).
