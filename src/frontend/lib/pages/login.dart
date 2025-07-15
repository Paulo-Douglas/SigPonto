import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../components/my_input.dart';
import '../components/my_button.dart';
import '../styles/colors.dart';
import "../service/service.dart";

class TelaLogin extends HookWidget {
  final double width;
  final double height;

  const TelaLogin({super.key, required this.width, required this.height});

  @override
  Widget build(BuildContext context) {
    final valueUserInput = useState<String>("");

    final credenciais = useListenable(SERVICE.credenciaisNotifier);

    useEffect(() {
      final token = credenciais.value["token"];
      if (token != null && token.toString().isNotEmpty) {
        Future.microtask(() {
          Navigator.pushNamed(context, "/home");
        });
      }
      return null;
    }, [credenciais.value]);

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
                        valueUserInput: valueUserInput,
                        login: (String value) {
                          SERVICE.login(value);
                        },
                      ),
                      MyButton(
                        actionButton: "Entrar",
                        onPressed: () => SERVICE.login(valueUserInput.value),
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
