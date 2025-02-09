package com.atguigu.spring6.resource.controller;

import com.atguigu.spring6.resource.service.UserService;
import jakarta.annotation.Resource;
import org.springframework.stereotype.Controller;

@Controller("myUserController")
public class UserController {

    // @Resource(name = "myUserService")
    // private UserService userService;

    @Resource(name = "myUserService")
    private UserService userService;

    public void add() {
        System.out.println("Controller.......");
        userService.add();
    }
}
