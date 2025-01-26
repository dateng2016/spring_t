
import com.atguigu.spring6.User;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.lang.reflect.InvocationTargetException;


public class DummyTest {

    @Test
    public void testUserObject() {
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("bean.xml");

        User user = (User) applicationContext.getBean("user");


        System.out.println(user);
        System.out.println("------------BREAK LINE-------------");
        user.add();
    }

    @Test
    public void testUserObject1() throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {

        Class clazz = Class.forName("com.atguigu.spring6.User");

        System.out.println("This is -testUserObject1- ------------");
        User user = (User) clazz.getDeclaredConstructor().newInstance();
        System.out.println(user);


    }

}
