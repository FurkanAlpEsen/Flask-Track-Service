# Track-Service
 Python Spotify Track Service

## About 
Web platformunda Spotify servisine erişerek türe göre ve şarkıcı adına göre arama yapabilirsiniz.
Python v3.9 programlama dili kullanılarak 'Flask' kütüphanesi ile yazılmıştır. 
Arayüzler HTML,CSS ve JS ile yapılmıştır.

Program, spotify API'a bağlanarak yapılan doğrulamanın sonucunda şarkı,albümler ve daha bir çok şeye erişim sağlamaktadır. 

## Setup
Programın çalıştırılabilmesi için python ortamının hazırlanması gerekmektedir.
Oluşturulan python çevresi üzerine Flask paketinin kurulması gerekmektedir. (pip install flask)
Flask paketi kurulduktan sonra komut arayüzünde "set FLASK_APP=track" komutu çalıştırılmalıdır.
Çalıştırılan komut ile artık kodumuzu sisteme tanıtmış oluyoruz.
Tüm sistemi ayağa kaldırabilmek için  "flask run" komutu kullanılmalıdır.
Program bilgisayarın local sunucusunda çalışmaya başlayacaktır. 
Linke tıklayarak veya bilgisayar üzerinde varsayılan tarayıcılar ile "http://127.0.0.1:5000/" adresine gidebilirsiniz.
Açılan sayfa üzerinde bulunan radio butonlar aracılığıyla şarkı türüne göre ve şarkıcı adına göre arama yapabilirsiniz.
Aramadan sonra yönlendirilen sayfada şarkılara ait detayları ve bir çok şeyi de göreceksiniz. (http://127.0.0.1:5000/tracks/rock vs.)
Başka aramalar yapmak için önceki sayfaya yani ana sayfaya dönmeniz gerekmektedir.



