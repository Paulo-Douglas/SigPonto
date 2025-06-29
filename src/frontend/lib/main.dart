import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import './pages/login.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;

    return MaterialApp(
      initialRoute: '/login',
      routes: {'/login': (context) => TelaLogin(height: height, width: width)},
    );
  }
}
