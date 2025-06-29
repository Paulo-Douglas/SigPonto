import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_button.dart';

class TelaHome extends HookWidget {
  final ValueNotifier<String> tokenUser;
  final double width;
  final double height;

  const TelaHome({
    super.key,
    required this.tokenUser,
    required this.width,
    required this.height,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("SIGPONTO"),
        leading: IconButton(
          icon: Icon(Icons.logout),
          onPressed: () {
            tokenUser.value = "";
            Navigator.pop(context);
          },
        ),
      ),
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(color: Colors.white70),
        child: Column(
          children: [
            Expanded(
              child: SizedBox(
                height: height * 0.5,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  spacing: 50,
                  children: [
                    MyButton(
                      actionButton: "Visualizar minhas presenças",
                      onPressed: () => Navigator.pushNamed(context, '/pontos'),
                    ),
                    MyButton(
                      actionButton: "Bater ponto",
                      onPressed: () => print("Bater ponto"),
                    ),
                  ],
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Image.asset("./images/ufrn-logo.png", width: width * 0.2),
            ),
          ],
        ),
      ),
    );
  }
}
