import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_input.dart';

class TelaLogin extends HookWidget {
  final double width;
  final double height;

  const TelaLogin({super.key, required this.width, required this.height});

  @override
  Widget build(BuildContext context) {
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
                  child: MyInput(
                    helpText: "Seu usuário do SIGAA",
                    label: "Insira seu usuário",
                    icon: Icons.login,
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
