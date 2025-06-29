import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_button.dart';

class TelaHome extends HookWidget {
  final ValueNotifier<String> tokenUser;

  const TelaHome({super.key, required this.tokenUser});

  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;

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
                      onPressed: () => print("Ponto batido"),
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
