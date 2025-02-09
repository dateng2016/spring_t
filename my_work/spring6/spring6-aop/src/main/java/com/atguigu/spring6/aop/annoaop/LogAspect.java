package com.atguigu.spring6.aop.annoaop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Component
@Aspect
public class LogAspect {
    @Before(value = "execution(public int com.atguigu.spring6.aop.annoaop.CalculatorImpl.*(..))")
    public void beforeMethod(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        Object[] args = joinPoint.getArgs();
        System.out.println("Logger-->前置通知，");
        System.out.println("Method name -> " + methodName);
        System.out.printf("Args -> %s\n", Arrays.toString(args));
    }
}
