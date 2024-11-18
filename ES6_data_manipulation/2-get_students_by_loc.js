export default function getStudentsByLocation(list, city) {
  return list.filter((std) => std.location === city);
}
