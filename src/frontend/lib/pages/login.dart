import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_input.dart';
import '../components/my_button.dart';
import '../utils/login_system.dart';
import '../styles/colors.dart';

class TelaLogin extends HookWidget {
  final double width;
  final double height;
  final ValueNotifier<String> tokenUser;
  final user;

  const TelaLogin({
    super.key,
    required this.width,
    required this.height,
    required this.tokenUser,
    required this.user,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).scaffoldBackgroundColor,
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
                    GetColor.blueLigth.color,
                    GetColor.blueLigthAlfa.color,
                  ],
                ),
                color: Theme.of(context).colorScheme.primary,
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
