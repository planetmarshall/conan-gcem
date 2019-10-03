#include <iostream>
#include <gcem.hpp>

int main() {

    constexpr auto x  = 10;
    constexpr auto f10 = gcem::factorial(x);

    std::cout << x << "! = " << f10 << std::endl;

    return 0;
}
