// okay rust, what's the weather like in san francisco?
fun weather = fun(ctx) {
    let (weather, _) = ctx.get("weather");
    if (weather == "sunny") {
        println("Go get your shorts and a cup of coffee");
    } else {
        println("You should get some shades");
    }
}

// that wasn't very useful... let's try again
// okay rust, what's the 521st prime number?
fun prime = fun(ctx) {
    let (prime, _) = ctx.get("prime");
    if (prime == "521") {
        println("You're a genious!");
    } else {
        println("You should try again");
    }
}

// okay, let's try again
// okay rust, what's the square root of 2?
fun sqrt = fun(ctx) {
    let (sqrt, _) = ctx.get("sqrt");
    if (sqrt == "1.4142135623730951") {
        println("You're a genious!");
    } else {
        println("You should try again");
    }
}

// i give up