# Who Actually Makes: open data

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23920936.svg)](https://doi.org/10.5281/zenodo.23920936)

Who makes store-brand products, from public records. Every list behind [Who Actually Makes](https://whoactuallymakes.com/): which company each Kirkland Signature product traces to, the companies behind store brands and the labels they're on record for, every NHTSA tire plant code, what tire makers and carmakers say about tire age, and the evidence, sources, corrections and update schedule behind it all.

**19 datasets · 15,748 records · version 2026-11-13** · JSON and CSV (UTF-8) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Live copy and API: https://whoactuallymakes.com/data/

Each answer on the site carries a stamp (confirmed, documented, reported or unverified) and links to the record it rests on. The evidence file keeps the exact quote, the date it was read and a SHA-256 fingerprint of the document, so anyone can check a row against its source. How the stamps work: https://whoactuallymakes.com/how-we-know/

## Datasets

| Dataset | Records | Updated | Files | On the site |
|---|---:|---|---|---|
| [Who makes what: store-brand answers (Kirkland Signature)](#claims) | 730 | 2026-11-11 | [JSON](data/claims.json) (644 KB) · [CSV](data/claims.csv) (398 KB) | [/kirkland-signature/](https://whoactuallymakes.com/kirkland-signature/) |
| [Companies behind store brands (maker pages)](#companies) | 14 | 2026-11-11 | [JSON](data/companies.json) (8 KB) · [CSV](data/companies.csv) (4 KB) | [/makers/](https://whoactuallymakes.com/makers/) |
| [Which store labels each company is on record for](#company-labels) | 214 | 2026-11-11 | [JSON](data/company-labels.json) (111 KB) · [CSV](data/company-labels.csv) (69 KB) | [/makers/](https://whoactuallymakes.com/makers/) |
| [Tire plant codes (NHTSA)](#tire-plants) | 1,246 | 2026-11-09 | [JSON](data/tire-plants.json) (149 KB) · [CSV](data/tire-plants.csv) (89 KB) | [/tire-dot-code-lookup/](https://whoactuallymakes.com/tire-dot-code-lookup/) |
| [Tire age guidance from tire makers, carmakers and agencies](#tire-age) | 22 | 2026-11-12 | [JSON](data/tire-age.json) (35 KB) · [CSV](data/tire-age.csv) (20 KB) | [/tire-date-code/](https://whoactuallymakes.com/tire-date-code/) |
| [Evidence records: every quote behind our answers](#evidence) | 1,694 | 2026-11-13 | [JSON](data/evidence.json) (1474 KB) · [CSV](data/evidence.csv) (1145 KB) | [/how-we-know/](https://whoactuallymakes.com/how-we-know/) |
| [Sources: the public records we use, and their limits](#sources) | 194 | 2026-11-13 | [JSON](data/sources.json) (217 KB) · [CSV](data/sources.csv) (89 KB) | [/sources/](https://whoactuallymakes.com/sources/) |
| [Corrections log](#corrections) | 54 | 2026-11-12 | [JSON](data/corrections.json) (46 KB) · [CSV](data/corrections.csv) (34 KB) | [/corrections/](https://whoactuallymakes.com/corrections/) |
| [Update schedule: when each list is checked](#schedule) | 57 | 2026-11-13 | [JSON](data/schedule.json) (338 KB) · [CSV](data/schedule.csv) (14 KB) | [/update-schedule/](https://whoactuallymakes.com/update-schedule/) |
| [Costco diaper prices: every size at every read](#costco-diaper-prices) | 60 | 2026-11-09 | [JSON](data/costco-diaper-prices.json) (18 KB) · [CSV](data/costco-diaper-prices.csv) (8 KB) | [/costco-diapers/](https://whoactuallymakes.com/costco-diapers/) |
| [Kirkland vs name brands: every pair and its verdict](#kirkland-vs-pairs) | 22 | 2026-11-09 | [JSON](data/kirkland-vs-pairs.json) (21 KB) · [CSV](data/kirkland-vs-pairs.csv) (8 KB) | [/kirkland-vs-name-brands/](https://whoactuallymakes.com/kirkland-vs-name-brands/) |
| [Car battery date code rules, by brand](#battery-date-codes) | 21 | 2026-11-07 | [JSON](data/battery-date-codes.json) (87 KB) · [CSV](data/battery-date-codes.csv) (4 KB) | [/battery-date-code/](https://whoactuallymakes.com/battery-date-code/) |
| [USDA meat, poultry and egg plants (FSIS directory)](#usda-establishments) | 7,257 | 2026-11-02 | [JSON](data/usda-establishments.json) (1621 KB) · [CSV](data/usda-establishments.csv) (1443 KB) | [/usda-establishment-number-lookup/](https://whoactuallymakes.com/usda-establishment-number-lookup/) |
| [Subaru, Kia and Toyota rows in NHTSA's AALA reports, model years 2018 on](#car-origin-filings) | 863 | 2026-11-13 | [JSON](data/car-origin-filings.json) (375 KB) · [CSV](data/car-origin-filings.csv) (119 KB) | [/where-is-subaru-made/](https://whoactuallymakes.com/where-is-subaru-made/) |
| [Insignia model numbers on California's appliance register](#insignia-register) | 714 | 2026-11-10 | [JSON](data/insignia-register.json) (213 KB) · [CSV](data/insignia-register.csv) (108 KB) | [/insignia/](https://whoactuallymakes.com/insignia/) |
| [Hart, Hyper Tough, Husky and Harbor Freight battery chargers on California's appliance register](#store-tools-register) | 657 | 2026-11-10 | [JSON](data/store-tools-register.json) (335 KB) · [CSV](data/store-tools-register.csv) (136 KB) | [/store-brand-tools/](https://whoactuallymakes.com/store-brand-tools/) |
| [Craftsman model numbers and the companies government records name for them](#craftsman-records) | 442 | 2026-11-10 | [JSON](data/craftsman-records.json) (153 KB) · [CSV](data/craftsman-records.csv) (96 KB) | [/craftsman/](https://whoactuallymakes.com/craftsman/) |
| [Onn TV model numbers and the manufacturers California's appliance register lists for them](#onn-tv-register) | 533 | 2026-11-10 | [JSON](data/onn-tv-register.json) (129 KB) · [CSV](data/onn-tv-register.csv) (56 KB) | [/onn-tv/](https://whoactuallymakes.com/onn-tv/) |
| [Trader Joe's wine, beer and spirits label approvals (TTB)](#trader-joes-alcohol) | 954 | 2026-11-11 | [JSON](data/trader-joes-alcohol.json) (498 KB) · [CSV](data/trader-joes-alcohol.csv) (265 KB) | [/trader-joes/](https://whoactuallymakes.com/trader-joes/) |

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
| `relation` | text | What the record says the company did, as one of these values (taken from the data, so the list is complete): approval-holder, bottled-by, distributed-by, fsc-label-holder, imported-by, label-holder, licensed-to, listed-maker, made-at, made-by, packed-by, recalled-by, registered-via, ttb-label-holder or usda-name-listed. A record never says more than its value: recalled-by names the recalling firm, label holders hold the label, and so on. |
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
| `link_kind` | text | Which kind of record links the company to the label, one of: api-oil-license, claim, fda-recall or state-pet-food-register. |
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
- **Kept fresh:** Re-read in a browser every year, and whenever a maker changes its advice
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
- **Based on:** 50 public sources, listed in `catalog.json` (`based_on`)
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

Each check we run on a schedule: what it reads, how often, by script or in a browser, when it last ran, when it’s next due and what it found.

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

<a id="costco-diaper-prices"></a>

### Costco diaper prices: every size at every read

The box price, count, offer and price per diaper for Kirkland Signature, Huggies Plus, Pampers Swaddlers Ultra, Pull-Ups and Easy Ups on Costco.com, one row per size per read, so prices can be followed over time.

- **Limits:** Online prices at one ZIP code on the day we read them. Warehouse prices can differ, and a gap between reads can hide a short offer.
- **Kept fresh:** Every time we re-read the listings
- **Rights:** CC BY covers our table. Product names belong to their owners.
- **Based on:** 9 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/costco-diaper-prices.json`, `data/costco-diaper-prices.csv` · live: https://whoactuallymakes.com/data/costco-diaper-prices.json

<details><summary>The 11 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `read_on` | date | The day we read the listing (YYYY-MM-DD). |
| `product` | text | The product as Costco lists it. |
| `size` | text | The size on the box. |
| `lb_from` | number | Lowest weight printed for this size, in pounds. Empty for Newborn. |
| `lb_to` | number | Highest weight printed. Empty if the size is open-ended, such as 27+. |
| `count` | number | Diapers or pants in the box. |
| `item` | text | Costco's item number. |
| `regular` | number | Regular box price in US dollars. |
| `offer` | number | Offer price that day. Empty if no offer showed. |
| `cents_each` | number | What was charged that day, per diaper, in US cents. |
| `url` | url | The Costco listing. |

</details>

<a id="kirkland-vs-pairs"></a>

### Kirkland vs name brands: every pair and its verdict

One row per pair of a Kirkland Signature product and a name brand: the verdict worked out from the records, the companies involved, and for medicines the FDA application, holder, strength and form on each label. Some pairs also carry Costco prices.

- **Limits:** These are the pairs people search for plus the brands Kirkland medicine labels name, not a sample of everything Costco sells. A same-company verdict doesn't prove the same factory or recipe, and a shared FDA application covers the label we read, not every pack.
- **Kept fresh:** Weekly, and when a label or claim changes
- **Rights:** CC BY covers our table. Product names belong to their owners.
- **Files:** `data/kirkland-vs-pairs.json`, `data/kirkland-vs-pairs.csv` · live: https://whoactuallymakes.com/data/kirkland-vs-pairs.json

<details><summary>The 29 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `pair` | text | Our ID for the pair. |
| `group` | text | Everyday or Medicine. |
| `category` | text | Aisle, such as Household or Medicine. |
| `kirkland_product` | text | The Kirkland Signature product. |
| `name_brand` | text | The name brand it is set against. |
| `name_brand_owner` | text | The company behind the name brand, or the company on its label. Empty if we have no record. |
| `verdict` | text | Our verdict, worked out from the records: Same plant, Same FDA application, Same company, Was, not now, Old record only, Different company or No record yet. |
| `stamp` | text | How strong the record is: documented or reported. Empty if the verdict rests on no maker claim. |
| `companies` | text | Companies the Kirkland product is tied to, split by \| when more than one. |
| `note` | text | The limit on this verdict, in a sentence. Often empty. |
| `same_active_ingredient` | boolean | true if the two medicines list the same active ingredient. Empty for everyday products and where they don't match. |
| `kirkland_strength` | text | Active ingredient and strength on the Kirkland label. |
| `name_brand_strength` | text | The same for the name-brand label. |
| `form` | text | Dosage form on the Kirkland label, such as powder or tablet. |
| `fda_application` | text | The FDA application number both labels list. Filled only when the verdict is Same FDA application. |
| `fda_holder` | text | The holder FDA gives for that application. Filled only with fda_application. |
| `other_fda_applications` | text | Other application numbers on the name brand's labels, split by \|. |
| `kirkland_label` | url | The Kirkland label on DailyMed. |
| `name_brand_label` | url | The name-brand label on DailyMed. |
| `record` | text | The kind of record behind an everyday verdict. |
| `record_covers` | text | What that record covers. |
| `record_date` | date | The date of that record, when it has one. |
| `price_unit` | text | What the prices are per, such as AA battery. Empty for pairs we didn't price. |
| `kirkland_cents` | number | Kirkland price per unit in US cents. |
| `name_brand_cents` | number | Name-brand price per unit in US cents. |
| `price_read_on` | date | The day those prices were read. |
| `evidence` | text | Evidence record IDs, split by \|. They match the Evidence file. |
| `answer_page` | url | Our page for the Kirkland product. |
| `read_on` | date | The day the pairs were last built from the records. |

</details>

<a id="battery-date-codes"></a>

### Car battery date code rules, by brand

How each brand dates its car batteries: where to look, the format, a worked example, and whether the rule comes from the maker or only from a third party.

- **Limits:** Rules are dated and can change. Some come only from a third party, and some brands have no rule. A date code shows when a battery was dated or shipped, not when you bought it, and most codes leave out the decade.
- **Kept fresh:** Every six months, and when a maker changes a rule
- **Rights:** CC BY covers our table. Brand names belong to their owners.
- **Files:** `data/battery-date-codes.json`, `data/battery-date-codes.csv` · live: https://whoactuallymakes.com/data/battery-date-codes.json

<details><summary>The 11 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `brand` | text | The battery brand. |
| `standing` | text | Where the rule comes from: From the maker, Part maker, part third-party, Third-party only, or No rule we trust. |
| `where_to_look` | text | Where the code sits on the battery. |
| `format` | text | How the code is built. |
| `example` | text | A worked example. Empty if we have no rule. |
| `example_means` | text | What the example reads as. |
| `date_marks` | text | What the date marks: Shipped, Made, or Not stated when the record does not say. |
| `source` | text | Who gives the rule. |
| `source_url` | url | The record. |
| `source_date` | date | The record's own date, when it has one. |
| `read_on` | date | The day we read the rule. |

</details>

<a id="usda-establishments"></a>

### USDA meat, poultry and egg plants (FSIS directory)

Every entry in USDA FSIS's Meat, Poultry and Egg Product Inspection Directory: the establishment number or numbers, the plant's name, other names listed, address, county, the work USDA lists, size band and grant date.

- **Limits:** A number names the plant that last processed a product under inspection, not the brand, the farm or every ingredient. Other names are as USDA lists them, and don't prove a plant made any one pack. Foreign plants and state-inspected plants aren't included.
- **Kept fresh:** Monthly, read in a browser from USDA's directory, then loaded here
- **Rights:** The directory is US government work (USDA FSIS), in the public domain in the US. CC BY covers our compiled file.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/usda-establishments.json`, `data/usda-establishments.csv` · live: https://whoactuallymakes.com/data/usda-establishments.json

<details><summary>The 14 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `code` | text | Every number the plant holds, joined with +, e.g. M18532+P18532. |
| `name` | text | The plant's name as USDA lists it. |
| `trade_names` | text | Other names USDA lists for the plant, separated by semicolons; blanks such as N/A removed. |
| `address` | text | Street address. |
| `city` | text | City. |
| `state` | text | Two-letter state or territory. |
| `postal_code` | text | ZIP code. |
| `county` | text | County. |
| `activities` | text | The work USDA lists at the plant. |
| `size` | text | USDA's size band: Very Small, Small, Large, N / A, or blank. |
| `grant_date` | text | Grant date as USDA lists it. Many show 2021, likely a system date, so don't read them as start dates. |
| `fsis_id` | text | USDA's internal ID for the plant. |
| `lat` | number | Latitude from USDA's file. |
| `lon` | number | Longitude from USDA's file. |

</details>

<a id="car-origin-filings"></a>

### Subaru, Kia and Toyota rows in NHTSA's AALA reports, model years 2018 on

Every row for a Subaru, Kia or Toyota car, by badge or by builder, in NHTSA's yearly Part 583 reports: US and Canadian parts share, top foreign parts sources, final assembly country, and engine and transmission origin.

- **Limits:** A row covers a whole model line, not one car, and a line can come from two plants. Shares are averages by value, mostly rounded to 5%. Empty cells were left blank in the report. Country letters are as filed: J Japan, K Korea, M or MX Mexico, US United States, CH China. Two letters joined with + mean the report printed both.
- **Kept fresh:** Monthly check for a new report, read in a browser
- **Rights:** The filings are US government work. CC BY covers our table. Brand names belong to their owners.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/car-origin-filings.json`, `data/car-origin-filings.csv` · live: https://whoactuallymakes.com/data/car-origin-filings.json

<details><summary>The 14 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `model_year` | number | Model year of the report |
| `manufacturer` | string | Manufacturer column as filed |
| `make` | string | Make column as filed |
| `carline` | string | Carline as filed |
| `vehicle_type` | string | PC or MPV as filed |
| `us_canada_pct` | number | Percent US and Canadian parts by value; empty if blank |
| `foreign_1_pct` | number | Largest foreign parts share |
| `foreign_1_country` | string | Its country letter; empty if not printed |
| `foreign_2_pct` | number | Second foreign parts share |
| `foreign_2_country` | string | Its country letter |
| `final_assembly` | string | Final assembly country letter |
| `engine` | string | Engine origin letter |
| `transmission` | string | Transmission origin letter |
| `report_url` | string | The NHTSA PDF |

</details>

<a id="insignia-register"></a>

### Insignia model numbers on California's appliance register

Every Insignia filing with a model number starting NS on the California Energy Commission's appliance register (MAEDbS): the company listed as manufacturer, the type, the date added and, for TVs, screen size and width in pixels.

- **Limits:** A filing names the company that told California it makes a model, not a look at any unit. Where Best Buy filed in its own name, no factory is listed. Filings under the Insignia brand with model numbers not starting NS are left out. Company names are as filed, with commas restored where the export replaced them.
- **Kept fresh:** Monthly, read in a browser from California's register, then loaded here
- **Rights:** Data from the California Energy Commission's Modernized Appliance Efficiency Database System. CC BY covers our compiled file; credit the California Energy Commission for the underlying records.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/insignia-register.json`, `data/insignia-register.csv` · live: https://whoactuallymakes.com/data/insignia-register.json

<details><summary>The 11 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `model` | text | The model number as filed. A * or a run of x stands for characters the filer left open. |
| `manufacturer_listed` | text | The company the filing lists as manufacturer; blank when Best Buy filed it in its own name. |
| `filed_by_best_buy` | boolean | True when the filer is Best Buy, so no factory is named. |
| `filer` | text | The manufacturer field exactly as the register holds it, Best Buy included. |
| `type` | text | Product type: Dehumidifier, Dishwasher, Dryer, Microwave or cooking, Portable air conditioner, Refrigerator or freezer, Room air conditioner, TV, Washer or Wine or beverage cooler. |
| `register_list` | text | Which list on the register the row came from. |
| `filed` | text | Date the filing was added (YYYY-MM-DD); blank where our copy lost it. |
| `screen_inches` | number | Diagonal screen size for TVs. |
| `width_px` | number | Horizontal pixel count, for TVs on the federally tested list. |
| `archived` | boolean | True for rows on the register's archived list. |
| `pattern` | boolean | True when the model number is a pattern rather than one model. |

</details>

<a id="store-tools-register"></a>

### Hart, Hyper Tough, Husky and Harbor Freight battery chargers on California's appliance register

Every battery-charger filing on the California Energy Commission's appliance register (MAEDbS) under Hart, Hyper Tough, Husky and Harbor Freight's brand names: the company listed as manufacturer, the charger, basic and product model numbers, the test battery's maker, model and voltage, the power supply's maker and the date added.

- **Limits:** A filing names the company that told California it makes a charger system, not a look at any unit, and not proof of who built the tool the charger ships with. Where Harbor Freight filed in its own name, no factory is listed. A filing counts for a brand when its brand field reads that name, as filed. Company names are as filed, with commas restored where the export replaced them.
- **Kept fresh:** Monthly, from California's register search, then loaded here
- **Rights:** Data from the California Energy Commission's Modernized Appliance Efficiency Database System. CC BY covers our compiled file; credit the California Energy Commission for the underlying records.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/store-tools-register.json`, `data/store-tools-register.csv` · live: https://whoactuallymakes.com/data/store-tools-register.json

<details><summary>The 17 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `store_brand` | text | The store brand family: Harbor Freight, Hart, Husky or Hyper Tough. |
| `brand_filed` | text | The brand field exactly as filed. |
| `manufacturer_listed` | text | The company the filing lists as manufacturer; blank when Harbor Freight filed it in its own name. |
| `filed_by_harbor_freight` | boolean | True when the filer is Harbor Freight, so no factory is named. |
| `filer` | text | The manufacturer field as the register holds it, Harbor Freight included. |
| `charger_models` | text | The charger model numbers on the filing, separated by semicolons. A * stands for characters the filer left open. |
| `basic_model` | text | The filing's basic model number. |
| `product_models` | text | Products the charger is sold with, where the filing lists them (small-charger list only). |
| `test_battery_maker` | text | The company the filing names as maker of the battery the charger was tested with. |
| `test_battery_models` | text | The test battery's model number. |
| `test_battery_volts` | number | The test battery's nameplate voltage. |
| `test_battery_wh` | number | The test battery's energy capacity in watt-hours. |
| `power_supply_maker` | text | The company the filing names as maker of the external power supply. |
| `product_type` | text | Product type, on the small-charger list. |
| `register_list` | text | Which list on the register the row came from: Federally regulated battery chargers or Small battery chargers (California). |
| `filed` | text | Date the filing was added (YYYY-MM-DD). |
| `archived` | boolean | True for rows on the register's archived list. |

</details>

<a id="craftsman-records"></a>

### Craftsman model numbers and the companies government records name for them

One row per record that ties a Craftsman model number to a company: battery-charger filings on California's appliance register (MAEDbS), EPA small-engine certificates from its 1997-2010 archive that list Craftsman or Sears models, and CPSC recalls that mention Craftsman. Each row gives the company, its role in the record, the year, the model numbers and, for Sears-era models, the three-digit Sears source code.

- **Limits:** A record names a company for the models it lists, not for every Craftsman product, and isn't a look at any unit. A charger filing names the company that filed it, which is often Stanley Black & Decker itself; an engine certificate names the engine's maker of record, not who assembled the tool; a recall names the manufacturer, importer or distributor as the CPSC gives them. Sellers (Sears, Kmart, Orchard Supply, Ace) are left out of the company column.
- **Kept fresh:** Monthly, from California's register, CPSC recalls and Stanley Black & Decker's newest SEC report
- **Rights:** Compiled from California Energy Commission, US EPA and US CPSC public records. CC BY covers our compiled file; credit the agencies for the underlying records.
- **Based on:** 3 public sources, listed in `catalog.json` (`based_on`)
- **Files:** `data/craftsman-records.json`, `data/craftsman-records.csv` · live: https://whoactuallymakes.com/data/craftsman-records.json

<details><summary>The 10 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `record` | text | Which record the row comes from: CPSC recall, California charger filing or EPA engine certificate. |
| `company` | text | The company the record names, as written there. |
| `role` | text | What the record says the company did. |
| `year` | text | Year the filing was added, the engine's model year or the recall date. |
| `model_numbers` | text | Model numbers the record lists, separated by semicolons. A * stands for characters a filer left open. |
| `sears_source_code` | text | For Sears-era model numbers, the three digits before the dot. |
| `also_named` | text | Another company the same record names, such as the test battery's maker. |
| `product` | text | What the record covers, in its own words where it gives them. |
| `reference` | text | The recall number or EPA engine family. |
| `url` | text | Where the record can be read. |

</details>

<a id="onn-tv-register"></a>

### Onn TV model numbers and the manufacturers California's appliance register lists for them

One row per Onn TV filing on California's appliance register (MAEDbS), from all three of its TV lists, approved and archived, under both spellings it holds (ONN and onn.). Each row gives the model number, the company listed as manufacturer, the list, the date filed and the screen size.

- **Limits:** A filing names the company that filed the model, not the factory of any one unit. The same Onn number is often filed by several companies, and the register doesn't say which built a given TV. Rows filed under ONN in 2014-15 by Shenyang Tongfang carry other brands' model numbers and are marked left_out_of_counts.
- **Kept fresh:** Monthly, from California's register
- **Rights:** Compiled from California Energy Commission public records. CC BY covers our compiled file; credit the agency for the underlying records.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/onn-tv-register.json`, `data/onn-tv-register.csv` · live: https://whoactuallymakes.com/data/onn-tv-register.json

<details><summary>The 9 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `model` | text | The model number as filed. A * stands for characters a filer left open. |
| `manufacturer_listed` | text | The company the filing lists as manufacturer, one spelling per company. |
| `brand_as_filed` | text | The brand field as filed: ONN or onn. |
| `register_list` | text | Which of the register's TV lists the row is on. |
| `filed` | date | Date the filing was added, where the list gives one. |
| `screen_inches` | number | Screen size in inches, where the list gives one. |
| `archived` | boolean | True for rows on the register's archived lists. |
| `pattern` | boolean | True when the model number holds open characters (*). |
| `left_out_of_counts` | boolean | True for the 2014-15 rows filed under ONN with other brands' model numbers. |

</details>

<a id="trader-joes-alcohol"></a>

### Trader Joe's wine, beer and spirits label approvals (TTB)

Every label approval in TTB's public COLA registry with a brand name starting "Trader Joe", for the 15 years the registry's search allows: the approval number, the kind of drink, TTB's class, the company that holds the approval (box 8 of the form), the trade name the form says goes on the bottle, origin, date and status, with a link to each form.

- **Limits:** An approval shows which company applied for a label and got it approved, not that the label is on shelves now, and not which of several holders filled the bottle in front of you. One approval covers one label design, so a new vintage or size adds a row; it is not a count of bottles. Six approvals whose form gave no applicant are left out. "holder" groups spellings and related Sazerac companies; "applicant" is as filed.
- **Kept fresh:** Read in full from TTB's registry when the page is re-checked (next May 2027)
- **Rights:** US government records in the public domain (TTB). CC BY covers our compiled file; credit TTB for the underlying approvals.
- **Based on:** 1 public source, listed in `catalog.json` (`based_on`)
- **Files:** `data/trader-joes-alcohol.json`, `data/trader-joes-alcohol.csv` · live: https://whoactuallymakes.com/data/trader-joes-alcohol.json

<details><summary>The 13 fields</summary>

| Field | Type | What it holds |
|---|---|---|
| `ttb_id` | text | TTB's approval number (TTB ID). |
| `kind` | text | Our grouping of TTB's class: Beer, Bourbon and American whiskey, Canadian whisky, Cocktails, Gin, Irish whiskey, Liqueurs, Mezcal, Other spirits, Other wine, Red wine, Rosé wine, Rum, Scotch whisky, Sparkling wine, Tequila, Vodka, White wine or Wine over 14% alcohol. TTB files still wine over 14% alcohol in its dessert wine class, shown here as "Wine over 14% alcohol". |
| `ttb_class` | text | TTB's class and type, as on the form. |
| `brand_on_form` | text | The brand name as filed. |
| `fanciful_name` | text | The fanciful name, if the form gives one. |
| `holder` | text | The holder, with spellings and related companies grouped. |
| `applicant` | text | The applicant name exactly as on the form (box 8). |
| `holder_place` | text | The holder's city and state as on the form. |
| `name_on_label` | text | The trade name the form says goes on the bottle, separated by semicolons; blank when the holder's own name is used. |
| `origin` | text | Origin as filed: a US state or a country. |
| `approved_on` | date | The date TTB approved the label. |
| `status` | text | The approval's status when read: Approved, Expired or Surrendered. |
| `form_url` | url | TTB's public copy of the form. |

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
