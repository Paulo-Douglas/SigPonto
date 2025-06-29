import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_input.dart';
import '../components/my_button.dart';
import '../utils/login_system.dart';

class TelaLogin extends HookWidget {
  final double width;
  final double height;
  final ValueNotifier<String> tokenUser;

  const TelaLogin({
    super.key,
    required this.width,
    required this.height,
    required this.tokenUser,
  });

  @override
  Widget build(BuildContext context) {
    var user = useState<String>("");

    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Image.asset(
              "./images/ufrn-logo.png",
              width: width * 0.5,
              height: height * 0.2,
            ),
            Container(
              width: width * 0.9,
              height: height * 0.5,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [
                    Colors.lightBlueAccent.withValues(blue: 10),
                    Colors.lightBlueAccent.withValues(blue: 10, alpha: 100),
                  ],
                ),
                color: Colors.blue,
                borderRadius: BorderRadius.circular(20),
              ),
              // color: Colors.amber,
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.all(12.0),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      MyInput(
                        helpText: "Seu usuário do SIGAA",
                        label: "Insira seu usuário",
                        icon: Icons.login,
                        user: user,
                        login: (String value) {
                          loginSystemSubmmit(
                            user,
                            tokenUser,
                            context,
                            value,
                            '/home',
                          );
                        },
                      ),
                      //abner.cordeiro
                      MyButton(
                        actionButton: "Entrar",
                        onPressed: () =>
                            loginSystemOnPressed(user, tokenUser, context),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            SizedBox(width: double.infinity, height: height * 0.2),
          ],
        ),
      ),
    );
  }
}
