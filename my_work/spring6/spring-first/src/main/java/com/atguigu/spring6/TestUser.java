package com.atguigu.spring6;

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.lang.reflect.InvocationTargetException;


public class TestUser {

    private Logger logger = LoggerFactory.getLogger(TestUser.class);

    @Test
    public void testUserObject() {
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("bean.xml");

        User user = (User) applicationContext.getBean("user");

        System.out.println(user);

        user.add();

        logger.info("EXECUTION SUCCESS!");

    }

    @Test
    public void testUserObject1() throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {

        Class clazz = Class.forName("com.atguigu.spring6.User");

        User user = (User) clazz.getDeclaredConstructor().newInstance();
        System.out.println(user);

    }
}
