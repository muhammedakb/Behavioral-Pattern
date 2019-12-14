# YAZILIM MİMARİSİ VE TASARIMI

BEHAVİORAL PATTERN

STRATEJİ

Strateji , bir algoritma ailesi tanımlamanıza, her birini ayrı bir sınıfa yerleştirmenize ve nesnelerini birbirleriyle değiştirmenize olanak sağlayan davranışsal bir tasarım desenidir.

SORUN

Bir gün rahat gezginler için bir navigasyon uygulaması oluşturmaya karar verdiniz. Uygulama, kullanıcıların hızlı bir şekilde kendilerini herhangi bir şehirde yönlendirmelerini sağlayan güzel bir harita etrafında toplandı.

Uygulama için en çok istenen özelliklerden biri otomatik rota planlamasıydı. Bir kullanıcı bir adres girebilmeli ve haritada görüntülenen hedefin en hızlı rotasını görebilmelidir.

Uygulamanın ilk sürümü yalnızca yollar üzerindeki rotaları oluşturabiliyordu. Araba ile seyahat eden insanlar neşeyle doluydu. Fakat görünüşe göre, herkes tatile çıkmayı sevmiyor. Böylece bir sonraki güncellemeyle, yürüyüş rotaları oluşturmak için bir seçenek eklediniz. Bundan hemen sonra, insanların toplu taşıma araçlarını rotalarında kullanmalarını sağlamak için başka bir seçenek eklediniz.

Ancak, bu sadece bir başlangıçtı. Daha sonra bisikletçiler için rota oluşturma eklemeyi planladınız. Ve daha sonra, bir kentin tüm turistik merkezlerinden geçen güzergahlar oluşturmak için başka bir seçenek.

![](https://refactoring.guru/images/patterns/diagrams/strategy/problem.png)

Bir iş perspektifinden uygulama başarılı olsa da, teknik kısım size birçok baş ağrısına neden oldu. Her yeni bir yönlendirme algoritması eklediğinizde, gezginin ana sınıfı iki katına çıktı. Bir noktada, canavarın bakımı çok zorlaştı.

Algoritmalardan herhangi birinde yapılan herhangi bir değişiklik, ister basit bir hata düzeltmesi, isterse sokak puanının hafif bir şekilde ayarlanması olsun, tüm sınıfı etkiledi ve çalışmakta olan kodda hata oluşturma şansını artırdı.

Buna ek olarak, takım çalışması verimsiz hale geldi. Başarılı sürümden hemen sonra işe alınan takım arkadaşlarınız, birleşme çatışmalarını çözmek için çok fazla zaman harcadıklarından şikayet ediyorlar. Yeni bir özellik uygulamak, diğer insanlar tarafından üretilen kodla çelişen aynı dev sınıfı değiştirmenizi gerektirir.

ÇÖZÜM

Strateji kalıbı, çok farklı şekillerde spesifik bir şeyler yapan bir sınıf almanızı ve tüm bu algoritmaları stratejiler adı verilen ayrı sınıflara çıkarmanızı önerir .

Bağlam adı verilen orijinal sınıf, stratejilerden birine referans saklamak için bir alana sahip olmalıdır. Bağlam, işi kendi başına yürütmek yerine bağlantılı bir strateji nesnesine devreder.

![](https://refactoring.guru/images/patterns/diagrams/strategy/solution.png)

Navigasyon uygulamamızda, her yönlendirme algoritması, tek bir buildRouteyöntemle kendi sınıfına çıkarılabilir . Yöntem bir başlangıç noktası ve varış yerini kabul eder ve rotanın kontrol noktalarının bir koleksiyonunu döndürür.

YAPI

![](https://refactoring.guru/images/patterns/diagrams/strategy/structure.png)

1)Bağlam sadece strateji arayüzü üzerinden bu cisimle beton stratejileri ve iletişim kurar birine başvuru içerir.

2)Strateji arayüzü tüm somut stratejiler için ortaktır. Bağlamın bir stratejiyi yürütmek için kullandığı bir yöntem ilan eder.

3)Somut Stratejiler , bağlamın kullandığı bir algoritmanın farklı çeşitlerini uygular

4)Bağlam, algoritmayı çalıştırması gereken her seferinde bağlantılı strateji nesnesinde yürütme yöntemini çağırır. Bağlam, ne tür bir strateji ile çalıştığını veya algoritmanın nasıl yürütüldüğünü bilmiyor.

5)Müşteri belli bir strateji nesnesi yaratır ve bağlama geçirir. Bağlam, istemcilerin çalışma zamanında bağlamla ilişkili stratejiyi değiştirmelerini sağlayan bir ayarlayıcı gösterir.


#KOD

Bu örnekte, bağlam çeşitli aritmetik işlemleri gerçekleştirmek için çoklu stratejiler kullanır .

// Strateji arayüzü herkes için ortak işlemler ilan etti
// Bazı algoritmaların desteklenen sürümleri. Bağlam bunu kullanır
// somut madde tarafından tanımlanan algoritmayı çağırmak için arayüz
// stratejiler

    interface Strategy is
        method execute(a, b)

// Somut stratejiler algoritmayı takip ederken uygular
// temel strateji arayüzü. Arayüz onları yapar
// bağlamda değiştirilebilir.

    class ConcreteStrategyAdd implements Strategy is
       method execute(a, b) is
           return a + b

    class ConcreteStrategySubtract implements Strategy is
       method execute(a, b) is
           return a - b

    class ConcreteStrategyMultiply implements Strategy is
        method execute(a, b) is
           return a * b

// Bağlam, müşterilere ilgi arayüzünü tanımlar.

    class Context is
    
   // Bağlam, stratejilerden birine referansta bulunur.
   // Bağlam bir somut sınıfını bilmiyor
   // Tüm stratejilerle birlikte çalışmalıdır.
   // strateji arayüzü.
   
    private strategy: Strategy

   // Genellikle bağlam, aracılığıyla bir strateji kabul eder.
   // yapıcı ve ayrıca bir ayarlayıcı sağlar
   // Strateji çalışma zamanında değiştirilebilir.
    method setStrategy(Strategy strategy) is
        this.strategy = strategy

   // Bağlam, bazı çalışmaları strateji nesnesine devreder
   // birden fazla sürümünü uygulamak yerine
   // algoritma kendi başınadır.
    
    method executeStrategy(int a, int b) is
        return strategy.execute(a, b)


// Müşteri kodu somut bir strateji seçer ve bunu iletir.
// Bağlam. Müşteri farklılıkların farkında olmalı
// Doğru seçimi yapabilmek için stratejiler arasında seçim.

    class ExampleApplication is
    method main() is
        Create context object.

       Read first number.
       Read last number.
       Read the desired action from user input.

        if (action == addition) then
            context.setStrategy(new ConcreteStrategyAdd())

        if (action == subtraction) then
            context.setStrategy(new ConcreteStrategySubtract())

        if (action == multiplication) then
            context.setStrategy(new ConcreteStrategyMultiply())

        result = context.executeStrategy(First number, Second number)

        Print result.



UYGULANABİLİRLİK

-Bir nesnenin içinde bir algoritmanın farklı değişkenlerini kullanmak ve çalışma zamanı sırasında bir algoritmadan diğerine geçmek istediğinizde Strateji desenini kullanın.
-Stratejiyi, yalnızca davranışlarını uyguladıkları şekilde farklı olan çok sayıda benzer sınıfınız olduğunda kullanın.
-Bir sınıfın iş mantığını, o mantık bağlamında önemli olmayabilecek algoritmaların uygulama ayrıntılarından ayırmak için modeli kullanın.
-Sınıfınızda, aynı algoritmanın farklı değişkenleri arasında geçiş yapan çok büyük bir koşullu işleç varsa deseni kullanın.

