# Uses rescursion the check if a report list is safe
def report_is_safe(report_list):
    if len(report_list) == 1:
        return True
    if (report_list[0] - report_list[1] < -3):
        return False
    if report_list[0] - report_list[1] >= 0:
        return False
    return report_is_safe(report_list[1:])



file_name = "input.txt"
total = 0

with open(file_name, 'r') as f:
    for report in f:
        report_list = report.split()
        report_list = list(map(int, report_list))
        if report_list[0] - report_list[1] > 0:
            report_list = report_list[::-1]
        if report_is_safe(report_list):
            total += 1

print(total)