fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    // println的几种输出格式
    println!("{}", x);
    println!("{:?}", x);
    println!("{:#?}", x);
    println!("{:4}", x);

    let _x = 5;
    // let y = 10;
    let _y = 10;

    // 变量解构
    let (a, mut b): (bool, bool) = (false, false);
    // a = true，不可变；b = true，可变
    println!("a = {:?}, b ] {:?}", a, b);

    b = true;
    assert_eq!(a, b);
}
