import 'package:flutter/material.dart';

enum GetColor {
  blueLigth,
  blueLigthAlfa,
  blue,
  green,
  greeLight,
  greeSuav,
  red,
  redLigth,
  white,
  background,
}

extension AppColor on GetColor {
  Color get color {
    switch (this) {
      case GetColor.blueLigth:
        return Colors.lightBlueAccent.withValues(blue: 10);
      case GetColor.blueLigthAlfa:
        return Colors.lightBlueAccent.withValues(blue: 10, alpha: 100);
      case GetColor.blue:
        return Colors.blue;
      case GetColor.green:
        return Colors.green.shade800;
      case GetColor.greeLight:
        return Colors.green.shade100;
      case GetColor.greeSuav:
        return Color.fromARGB(255, 10, 200, 100);
      case GetColor.red:
        return Colors.red.shade800;
      case GetColor.redLigth:
        return Colors.red.shade100;
      case GetColor.white:
        return Colors.white70;
      case GetColor.background:
        return const Color.fromARGB(255, 228, 228, 228);
    }
  }
}
