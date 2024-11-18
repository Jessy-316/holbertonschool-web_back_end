export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((stdnt) => stdnt.location === city)
    .map((stdnt) => {
      const stdntGrade = newGrades.find((grade) => grade.studentId === stdnt.id);
      return { ...stdnt, grade: stdntGrade ? stdntGrade.grade : 'N/A' };
    });
}
