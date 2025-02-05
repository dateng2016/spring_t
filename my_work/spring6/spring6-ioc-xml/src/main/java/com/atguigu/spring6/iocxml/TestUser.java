package com.atguigu.spring6.iocxml;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestUser {

    public static void main(String[] args) {
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean.xml");
        User user1 = (User) context.getBean("user");
        System.out.println("1. Getting Bean by ID -> " + user1);
        System.out.println("*****************************");
        User user2 = context.getBean(User.class);
        System.out.println("2. Getting Bean by ID -> " + user2);
        User user3 = context.getBean("user",User.class);
        System.out.println("3. Getting Bean by ID -> " + user3);
    }
}  
