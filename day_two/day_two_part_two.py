# Uses rescursion the check if an ascending report list is safe
def report_is_safe(report_list):
    if len(report_list) == 1:
        return True
    if (report_list[0] - report_list[1] < -3) or (report_list[0] - report_list[1] >= 0):
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
        else:
            works = False
            for i in range(len(report_list)):

                new_list = report_list[:i] + report_list[i+1:]
                if new_list[0] - new_list[1] > 0:
                    new_list = new_list[::-1]
                if report_is_safe(new_list):
                    works = True
            if works:
                total += 1

print(total)