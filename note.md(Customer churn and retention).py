Layihənin texniki hissəsi:

Layihəyə başlamaq üçün Telco Customer Churn datasetini Power BI-a import etdim, amma load etməmişdən qabaq Power Query-də datasetlə tanış oldum.
Dataset 7043 sətir və 21 sütundan ibarətdir. Power Query vasitəsilə sütunların tiplərinə baxdım və ehtiyac olduqda doğru tipə çevirdim,
dublikat və null dəyərlərə baxdım,TotalCharges-də null dəyərləri 0 ilə əvəz etdim.
Daha sonra Power Query-də TenureBand, MonthlyCharges, ChurnFlag sütunlarını yaratdım.
Close & Apply edərək dataseti Power BI-a yüklədim. Müxtəlif kateqoriyalar üzrə vizuallaşdırmalar aparmaq üçün yaratdığım measure-lər:

1. Ümumi müştərilərin sayı üçün Total Customers.
2. Şirkəti tərk edən müştərilərin sayı üçün Churned Customers.
3. İtkinin faizinə baxmaq üçün Churn Rate.
4. Müştərilərin orta aylıq ödənişinə baxmaq üçün Avg Monthly Charges.
5. Şirkəti tərk edən müştərilər nəticəsində yaranan itkinin məbləğinə baxmaq üçün Revenue Risk.

Bu measure-ləri yaradanda əsasən CALCULATE, DIVIDE, SUM, AVG, COUNTROWS funksiyalarından istifadə etdim.

Daha sonra bu measure-lərdən istifadə edərək dashboard hazırladım.
Dashboard-da 4 KPI var (Total Customers, Avg Charges, Churn Rate, Revenue Risk).
Həmçinin 4 kateqoriya (Contract, Internet Service, Payment Method, TenureBand) üçün Churn Rate-ləri göstərən bar chart-lar yaratdım.

Daha sonra slicer-lər vasitəsilə bar chart-ların müxtəlif kateqoriyalar üzrə faiz dəyişikliklərinə baxdım.
Slicer-lərdən istifadəni rahatlaşdırmaq üçün Reset Bookmark əlavə etdim və bu bookmark vasitəsilə dashboard-u ilkin vəziyyətinə qaytarmaq olar.
4 bar chart-dan əlavə, vizuallaşdırma üçün Matrix-dən istifadə etdim və Contract, Internet Service kateqoriyaları üzrə churn faizlərinə baxdım.
Matrix-ə Conditional Formatting tətbiq edərək 26,54 faizdən yüksək churn faizlərini mavi rənglə fərqləndirdim.
Eyni zamanda Churn Rate by Contract bar chart-ına Tooltip əlavə etdim. Bu Tooltip vasitəsilə Contract-lar üzrə yalnız Churn Rate-lərə deyil, 
həmçinin itirilən müştəriyə və itirilən məbləğə də rahatlıqla baxmaq olur.
3 slicer-dən əlavə olaraq What-if slicer-i də əlavə etdim. 
Məqsədim o idi ki, Churn Rate-lər dəyişən zaman itirdiyimiz müştərini və itirdiyimiz məbləği nə qədər azalda biləcəyimizi görək.

Business insight'lar:
1. Ümumilikdə 7043 müştəri var və hər bir müştəri orta hesabla 65 dollar məbləğində ödəniş edir.
2. TenureBand-a əsasən, müştərilərin 47%-i 1 ilini tamamlamamış şirkəti tərk edib və bu,TenureBand'a əsasən ən yüksək göstəricidir.
3. Ən sadiq müştərilər isə şirkətdə 49 ayını tamamlamış müştərilərdir və 9,51% Churn Rate-ə malikdirlər.
4. Normal olaraq, 43% Churn Rate göstəricisi ilə Month-to-month kateqoriyası birincidir.
5. Month-to-month kateqoriyasında 3875 müştəridən 1655-i şirkəti tərk edib və bu da 120K itki ilə nəticələnib.
6. One year kateqoriyasında isə bu itki 14K-ya qədərdir.
7. Ödəniş metodlarında Electronic check 45%-lə, internet servislərində isə Fiber optic 42%-lə birincidir.
8. Fiber optic servisindən istifadə edən və 1 aylıq müqavilələri olan müştərilər 54,61%-lə ən yüksək Churn Rate göstəricisinə malikdirlər.
9. Churn Rate göstəricisini 20% azaltdıqda isə 374 müştəri itkisinin və 27K aylıq gəlir itkisinin qarşısını ala bilərik.


Aldığım nəticələr və tövsiyələrim:
1.TenureBand hissəsində problem ilk 12 ayda görünür. 
Buna görə də fikrimcə, ilk 12 ay ərzində təqdim olunan xidmətlər və müştərilərin bu xidmətlərə münasibəti araşdırılmalıdır.
2.Eyni zamanda, nəyə görə müştərilərin 1 və ya 2 illik müqavilələri deyil, aylıq müqavilələri üstün tutduğu araşdırılmalıdır. 
Bunun səbəbi digər müqavilələrin şərtlərinin əlverişli olmaması ola bilər və bir müştəri 1 illik müqavilə yerinə 12 ay ardıcıl olaraq 1 aylıq müqavilə imzalaya bilər.
3.Aylıq müqavilələrdə ən çox itki Fiber optic servisi üzrədir. Həmin servis araşdırılmalıdır.Çünki həmin servisə digər kateqoriyalar üzrə baxdıqda da fərqin ciddi artdığını görürük.
Məsələn,araşdırma nəticəsində servisin xidmət haqqı çoxdursa azaldılmalı və ya texniki problemlər çox yaranırsa , aradan qaldırılmalıdır.
4. 1 və 2 illik müqavilə imzalayan müştərilər əsasən şirkətdəki xidmətlərdən çox uzun müddətdir istifadə edən müştərilərdir.
Buna görə də ilk 0-12 ay ərzində müştərilər nəzarətdə saxlanılmalı və şirkətə olan güvən artırılmalıdır.