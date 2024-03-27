#HOMEWORK
** PYTEST 'deki DEKORATÖRLER **
* pytest kütüphanesinde, test fonksiyonlarına özel davranışlar eklemek ve test koşullarını özelleştirmek için kullanılan çeşitli dekoratörler bulunmaktadır. İşte bazı yaygın pytest dekoratörleri:

@pytest.fixture: Bu dekoratör, test fonksiyonlarına veri sağlamak veya test koşullarını yapılandırmak için kullanılır. Örneğin, bir veritabanı bağlantısı oluşturmak veya test verilerini hazırlamak için kullanılabilir.

@pytest.mark.parametrize: Bu dekoratör, bir test fonksiyonunu belirli parametre değerleriyle birden çok kez çalıştırmak için kullanılır. Parametreler, test fonksiyonuna geçirilen argümanlar olarak işlev görür.

@pytest.mark.skip: Bu dekoratör, belirli bir testin çalıştırılmasını geçici olarak atlamak için kullanılır. Bir test koşulu karşılanmadığında veya belirli bir durumda testin geçersiz olduğu durumlarda kullanılabilir.

@pytest.mark.skipif: Bu dekoratör, belirli bir testin çalıştırılmasını koşula bağlı olarak atlamak için kullanılır. Bir koşul doğruysa, testi atlar.

@pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi belirtmek için kullanılır. Başarısız testler, test raporlarında 'xfail' olarak işaretlenir.*
