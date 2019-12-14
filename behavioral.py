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