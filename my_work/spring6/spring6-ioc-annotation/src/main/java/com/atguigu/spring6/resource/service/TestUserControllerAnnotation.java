package com.atguigu.spring6.resource.service;

import com.atguigu.spring6.config.SpringConfig;
import com.atguigu.spring6.resource.controller.UserController;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class TestUserControllerAnnotation {
    public static void main(String[] args) {
        ApplicationContext context =
                new AnnotationConfigApplicationContext(SpringConfig.class);
        UserController controller = context.getBean(UserController.class);
        controller.add();
    }
}
