import 'package:intl/intl.dart';

String formatarData(String dataString) {
  DateTime data = DateTime.parse(dataString);
  return DateFormat('dd/MM/yy HH:mm').format(data);
}
