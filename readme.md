## Розшифрування XML податкової накладної:
DECLARHEAD  
TIN - Індивідуальний номер платника податку  
C_DOC - J12 - Код документу, позначення документа для податкової  
C_DOC_SUB - 010 - Підтип документу, позначення документа для податкової  
C_DOC_VER - 13 - Номер версії документу, позначення документа для податкової  
C_DOC_TYPE - 0 - Номер звітного чи уточнюючого документу (для першого - 0)  
C_DOC_CNT - 100 - Номер документу в періоді, порядковий номер кожного однотипного документу в цьому періоді    
C_REG - 9 - Код області, Івано-Франківська  
C_RAJ - 15 - Код району  
PERIOD_MONTH - Звітний місяць, для місяців - порядковий номер місяця  
PERIOD_TYPE - Тип звітного періоду. 1-місяць, 2-квартал, 3-півріччя, 4-дев'ять місяців, 5-рік  
PERIOD_YEAR - Звітний рік  
C_STI_ORIG - Код ДПІ, в яку подається документ  
C_DOC_STAN - Стан документу. 1-звітний, 2-новий звітний, 3-уточнюючий  
LINKED_DOCS - Зв'язані документи  
D_FILL - Дата заповнення документа ddmmyyyy  
SOFTWARE - Ідентифікатор ПЗ за допомогою якого сформовано звіт  
/DECLARHEAD  

Всі елементи DECLARHEAD (крім SOFTWARE і LINKED_DOCS) повинні мати значення.  

DECLARBODY
R01G1 - Зведена податкова накладна
R03G10S - Складена на операції, звільнені від оподаткування
HORIG1 - Не підлягає виданню отримувачу (покупцю) з причини
HTYPR - Зазначається відповідний тип причини
HFILL - Дата виписки ПН
HNUM - Порядковий номер ПН
HNAMESEL - Постачальник (продавець) (найменування)
HNAMEBUY - Отримувач (покупець) (найменування) Неплатник
HKSEL - ІПН підприємства

/DECLARBODY