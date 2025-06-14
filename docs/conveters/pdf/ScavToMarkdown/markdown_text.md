
# Design and build accessible PDF tables
## Sample tables

---

### Table 1

| **Column header (TH)** | **Column header (TH)** | **Column header (TH)** |
|------------------------|------------------------|------------------------|
| **Row header (TH)**    | Data cell (TD)         | Data cell (TD)         |
| **Row header(TH)**     | Data cell (TD)         | Data cell (TD)         |

---

### Table 2: example of footnotes referenced from within a table

| **Expenditure by function £ million** | **2009/10** | **2010/11 ¹** |
|---------------------------------------|-------------|---------------|
| **Policy functions**                  |             |               |
| Financial                             | 22.5        | 30.57         |
| Information ²                         | 10.2        | 14.8          |
| Contingency                           | 2.6         | 1.2           |
| **Remunerated functions**             |             |               |
| Agency services ³                     | 44.7        | 35.91         |
| Payments                              | 22.41       | 19.88         |
| Banking                               | 22.90       | 44.23         |
| Other                                 | 12.69       | 10.32         |

(1) Provisional total as of publication date.  
(2) Costs associated with on-going information programmes.  
(3) From the management accounts, net of recoveries, including interest charges.

---

### Table 3: "film credits" style layout

| **Main character** | Daniel Radcliffe   |
|--------------------|-------------------|
| **Sidekick 1**     | Rupert Grint      |
| **Sidekick 2**     | Emma Watson       |
| **Lovable ogre**   | Robbie Coltrane   |
| **Professor**      | Maggie Smith      |
| **Headmaster**     | Richard Harris    |



**Table 4: table 3 with column headers added**

| Role             | Actor           |
|------------------|----------------|
| Main character   | Daniel Radcliffe|
| Sidekick 1       | Rupert Grint    |
| Sidekick 2       | Emma Watson     |
| Lovable ogre     | Robbie Coltrane |
| Professor        | Maggie Smith    |
| Headmaster       | Richard Harris  |


**Table 5: year-end financial statement (£, thousands)**

|                      | 2010 | 2009 | 2008 |
|----------------------|------|------|------|
| **Non-current assets** |      |      |      |
| Property             | 345  | 445  | 222  |
| Investment           | 567  | 654  | 423  |
| Intangibles          | 423  | 123  | 453  |
| **Current assets**     |      |      |      |
| Trade and other receivables | 435  | 634  | 231  |
| Cash and cash equivalents   | 524  | 123  | 482  |
| Other                | 223  | 211  | 254  |


**Table 6: a table with a more serious headings problem**

| Rainfall (inches) | Americas | Asia | Europe | Africa |
|-------------------|----------|------|--------|--------|
|                   |          |      |        |        |
| **2010**          |          |      |        |        |
| Average           | 104      | 201  | 193    | 144    |
| 24 hour high      | 15       | 26   | 27     | 18     |
| 12 hour high      | 9        | 10   | 11     | 12     |
|                   |          |      |        |        |
| **2009**          |          |      |        |        |
| Average           | 133      | 244  | 155    | 166    |
| 24 hour high      | 27       | 28   | 29     | 20     |
| 12 hour high      | 11       | 12   | 13     | 16     |


**Table 7: year-end statement, non-current assets (£, thousands)**

| Non-current assets | 2010 | 2009 | 2008 |
|--------------------|------|------|------|
| Property           | 345  | 445  | 222  |
| Investment         | 567  | 654  | 423  |
| Intangibles        | 423  | 123  | 453  |

**Table 8: year-end statement, current assets (£, thousands)**

| Current assets            | 2010 | 2009 | 2008 |
|---------------------------|------|------|------|
| Trade and other receivables| 435  | 634  | 231  |
| Cash and cash equivalents | 524  | 123  | 482  |
| Other                     | 223  | 211  | 254  |

**Table 9: rainfall by continent, 2009**

| Rainfall (inches) | Americas | Asia | Europe | Africa |
|-------------------|----------|------|--------|--------|
| Average           | 133      | 244  | 155    | 166    |
| 24 hour high      | 27       | 28   | 29     | 20     |
| 12 hour high      | 11       | 12   | 13     | 16     |


Table 10: self-contained year-end statement (£, thousands) (multiple layout problems)

|                        | 2011     | 2010 restated |
|------------------------|----------|---------------|
| **General income**     | 250,000  | 200,000       |
| **Increase in value, WIP** | 15,000   | 30,000        |
|                        | **265,000** | **230,000**   |
| **Administrative costs** |          |               |
| Staff costs            | (200,000) | (150,000)     |
| Early departures       | (10,000)  | (20,000)      |
| Other                  | (25,000)  | (10,000)      |
| Depreciation           | (10,000)  | (10,000)      |
| **Programme costs**    |           |               |
| Impairment loss        | (10,000)  | (5,000)       |
| Other                  | (5,000)   | (5,000)       |
|                        | (260,000) | (200,000)     |
| **Surplus**            | **5,000** | **30,000**    |


Table 11: self-contained year-end statement (£, thousands) (multiple problems resolved)

|                        | 2011     | 2010 restated |
|------------------------|----------|---------------|
| **Income**             |          |               |
| General income         | 250,000  | 200,000       |
| Increase in value      | 15,000   | 30,000        |
| **Total income**       | **265,000** | **230,000**   |
| **Administrative costs** |          |               |
| Staff costs            | (200,000) | (150,000)     |
| Early departures       | (10,000)  | (20,000)      |
| Other operating costs  | (25,000)  | (10,000)      |
| Depreciation           | (10,000)  | (10,000)      |
| **Programme costs**    |           |               |
| Impairment loss        | (10,000)  | (5,000)       |
| Other                  | (5,000)   | (5,000)       |
| **Total costs**        | (260,000) | (200,000)     |
| **Surplus**            | **5,000** | **30,000**    |


**Table 12: merged data cells are not recommended**

|        |      2008      |      |      2009      |      |
|--------|:--------------:|:----:|:--------------:|:----:|
| Name   | Yes            | No   | Yes            | No   |
| Bob    | 2              | 5    | 6              | 7    |
| Sue    | 3              | 8    | 4              | 7    |
| Sam    | [data relating to both columns in a single cell spanning both] |      | [data relating to both columns in a single cell spanning both] |      |

---

**Table 13: use of graphic symbols**

| Question                    | Respondent A | Respondent B | Respondent C |
|-----------------------------|:------------:|:------------:|:------------:|
| Are you a UK citizen?       | ☒            | ✓            | ☒            |
| Are you currently employed? | ✓            | ☒            | ✓            |
| Do you have a driving licence? | ☒        | ☒            | ✓            |

---

**Table 14: symbols replaced by real text**

| Question                    | Respondent A | Respondent B | Respondent C |
|-----------------------------|:------------:|:------------:|:------------:|
| Are you a UK citizen?       | No           | Yes          | No           |
| Are you currently employed? | Yes          | No           | Yes          |
| Do you have a driving licence? | No        | No           | Yes          |

---

**Table 15: courses offered by Institution X. A = Bachelor of Science, B = Bachelor of Arts, C = Masters, D = Doctorate, E = Diploma**

|                        | 2006 | 2007 | 2008 | 2009 |
|------------------------|:----:|:----:|:----:|:----:|
| Economics              | A, B | A, C | A, B | A, C |
| International relations| A, E | A, E | A, B | A, E |
| Philosophy             | A    | A    | A    | A, D |
| Politics               | A, D | A, D | A, D | A    |
| Mathematics            | B, C | B    | A, E | A, B |
| English                | A, C | A, B | A, B | C    |



**Table 16: Masters courses offered by Institution X**

|                        | 2006 | 2007 | 2008 | 2009 |
|------------------------|------|------|------|------|
| Economics              | No   | Yes  | Yes  | Yes  |
| International relations| No   | No   | No   | No   |
| Philosophy             | No   | No   | No   | No   |
| Politics               | No   | No   | No   | No   |
| Mathematics            | Yes  | No   | No   | No   |
| English                | Yes  | Yes  | Yes  | Yes  |


**Table 17: accounts, 2011 (£, thousands)**

| Accounting item         | 2011      |
|------------------------|-----------|
| **Income**             |           |
| General income         | 200,000   |
| Increase in value, WIP | 30,000    |
| **Income subtotal**    | **230,000**|
| **Administrative costs**|           |
| Staff                  | 150,000   |
| Early departures       | 20,000    |
| Other operating costs  | 10,000    |
| Depreciation           | 10,000    |
| **Programme costs**    |           |
| Impairment loss        | 10,000    |
| **Costs subtotal**     | **200,000**|
| **Balance**            | **30,000**|


**Table 18: accounts, 2011 (£, thousands)**

| Accounting item         | 2011        |
|------------------------|-------------|
| **Income**             |             |
| General income         | 200,000     |
| Increase in value, WIP | 30,000      |
| **Income subtotal**    | 230,000     |
| **Administrative costs**|             |
| Staff                  | (150,000)   |
| Early departures       | (20,000)    |
| Other operating costs  | (10,000)    |
| Depreciation           | (10,000)    |
| **Programme costs**    |             |
| Impairment loss        | (10,000)    |
| **Costs subtotal**     | (200,000)   |
| **Balance**            | 30,000      |


Table 19: Human Development Index (HDI)  
trends, 1980 to 2010. Source: Barro-Lee March, 2010

| Country      | 1980 | 1990 | 2000 | 2010  |
|--------------|------|------|------|-------|
| Afghanistan  | 0.78 | 1.48 | 2.16 | 3.33  |
| Albania      | 8.89 | 9.67 | 9.89 | 10.38 |
| Algeria      | 4.74 | 3.33 | 5.50 | 7.24  |
| Andorra      | 4.98 | 5.63 | 9.09 | 10.35 |
| Angola       |  -   |  -   | 4.42 | 4.42  |


Table 20: footnotes referenced from within a table

| Expenditure by function £million | 2009/10 | 2010/11¹ |
|----------------------------------|---------|----------|
| **Policy functions**             |         |          |
| Financial                        | 22.5    | 30.57    |
| Information²                     | 10.2    | 14.8     |
| Contingency                      | 2.6     | 1.2      |
| **Remunerated functions**        |         |          |
| Agency services³                 | 44.7    | 35.91    |
| Payments                         | 22.41   | 19.88    |
| Banking                          | 22.90   | 44.23    |
| Other                            | 12.69   | 10.32    |

---

¹ Provisional total as of publication date.  
² Costs associated with on-going information programmes.  
³ From the management accounts, net of recoveries and including interest charges


**Table 21: footnotes replaced by additional table summary text**

| Expenditure by function £million | 2009/10 | 2010/11 |
|----------------------------------|---------|---------|
| **Policy functions**             |         |         |
| Financial                        | 22.5    | 30.57   |
| Information                      | 10.2    | 14.8    |
| Contingency                      | 2.6     | 1.2     |
| **Remunerated functions**        |         |         |
| Agency services                  | 44.7    | 35.91   |
| Payments                         | 22.41   | 19.88   |
| Banking                          | 22.90   | 44.23   |
| Other                            | 12.69   | 10.32   |

---

**Table 22: referencing multiple endnotes from within a table**

| Expenditure £m     | Notes                        | 2010   | 2011   |
|--------------------|-----------------------------|--------|--------|
|                    | (Notes located on page [n])  |        |        |
| Information        | 1                            | 10.2   | 14.8   |
| Contingency        |                              | 2.6    | 1.2    |
| Payments           | 3                            | 22.41  | 19.88  |
| Banking services   | 4                            | 22.90  | 44.23  |
| Interest           |                              | 0.23   | 0.10   |
| Dividends          | 23                           | 2.5    | 3.68   |
| Other              | 9                            | 12.69  | 10.32  |

---

**Table 23: simulated table created using tabs and containing no structure**

|        |      | 2008         |      | 2009         |      |
|--------|------|--------------|------|--------------|------|
| Name   |      | Entered      | Completed | Entered      | Completed |
| Bob    |      | 22           | 21   | 20           | 19   |
| Sue    |      | 44           | 12   | 12           | 10   |


Table 24: year-end financial statement (£, thousands)

|                        | 2010 | 2009 | 2008 |
|------------------------|------|------|------|
| **Non-current assets** |      |      |      |
| **Buildings**          | 345  | 445  | 222  |
| **Investment**         | 567  | 654  | 423  |
| **Intangibles**        | 423  | 123  | 453  |
| **Current assets**     |      |      |      |
| Trade                  | 435  | 634  | 231  |
| Cash                   | 524  | 123  | 482  |
| Other                  | 223  | 211  | 254  |
| **Current liabilities**|      |      |      |
| Trade liabilities      | 154  | 125  | 421  |
| Financial debt         | 231  | 474  | 572  |
| Provisions             | 111  | 312  | 347  |


Table 25: setting column and row scope via the tags panel

|        | \multicolumn{2}{c|}{2008} | \multicolumn{2}{c|}{2009} |
|--------|---------|-----|---------|-----|
| Name   | Entered | Won | Entered | Won |
| Bob    | 22      | 21  | 20      | 19  |
| Sue    | 44      | 12  | 12      | 10  |
| Sam    | 16      | 4   | 45      | 30  |


Table 26: courses offered by Institution X. A = Bachelor of Science, B = Bachelor of Arts, C = Masters, D = Doctorate, E = Diploma

|                      | 2006 | 2007 | 2008 | 2009 |
|----------------------|------|------|------|------|
| **Economics**        | A, B | A, C | A, C | A, C |
| **International relations** | A, E | A, E | A, B | A, B |
| **Philosophy**       | A    | A    | A    | A    |
| **Politics**         | A, D | A, D | A, B | A    |
| **Mathematics**      | B, C | B    | A, B | A, B |
| **English**          | A, C | A, B | A, B | A, C |



**Table 27: “table” with columns simulated by using tab stops**

| Name                                   | Apples | Pears |
|-----------------------------------------|--------|-------|
| Bob Scott                              | 20     | 25    |
| Susan. P. Arnold-Jones, BA, FRSA, MD   | 24     | 15    |
| Sam Holder-Dickinson                   | 14     | 10    |

**Table 28: year-end financial table (£, thousands) – headings problem revisited**

|                        | 2010 | 2009 | 2008 |
|------------------------|------|------|------|
| **Non-current assets** |      |      |      |
| Buildings              | 345  | 445  | 222  |
| Investment             | 567  | 654  | 423  |
| Intangibles            | 423  | 123  | 453  |
| **Current assets**     |      |      |      |
| Trade                  | 435  | 634  | 231  |
| Cash                   | 524  | 123  | 482  |
| Other                  | 223  | 211  | 254  |
| **Current liabilities**|      |      |      |
| Trade liabilities      | 154  | 125  | 421  |
| **Financial debt**     | 231  | 474  | 572  |
| **Provisions**         | 111  | 312  | 347  |



**Table 29: multiple headers attributes for each data cell**

|                  | South America | Asia   | Africa | Australia |
|------------------|--------------|--------|--------|-----------|
| **2010**         |              |        |        |           |
| Highest average  | 523.6        | 467.4  | 405.0  | 340.5     |
| Highest in 24 hours | 73.1      | 54.1   | 27.2   | 66.3      |
| Highest in 12 hours | 42.4      | 30.1   | 15.9   | 40.3      |
| **2009**         |              |        |        |           |
| Highest average  | 487.7        | 453.6  | 398.7  | 356       |
| Highest in 24 hours | 67.2      | 53.2   | 44.3   | 53.8      |
| Highest in 12 hours | 34.7      | 34.1   | 29.8   | 31.0      |
| **2008**         |              |        |        |           |
| Highest average  | 496.7        | 444.3  | 502.1  | 399.6     |
| Highest in 24 hours | 44.2      | 56.7   | 32.1   | 63.2      |
| Highest in 12 hours | 30.1      | 32.7   | 21.9   | 40.2      |


