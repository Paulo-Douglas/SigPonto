import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:frontend/pages/pontos.dart';
import './pages/login.dart';
import './pages/home.dart';

void main() async {
  await dotenv.load(fileName: ".env");
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;

    return MaterialApp(
      initialRoute: '/login',
      routes: {
        '/login': (context) => TelaLogin(height: height, width: width),
        '/home': (context) => TelaHome(),
        '/pontos': (context) => TelaRelatorio(),
      },
    );
  }
}
