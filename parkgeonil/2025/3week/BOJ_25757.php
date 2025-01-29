<?php
// 한 줄 입력받기
$input = trim(fgets(STDIN));

// 공백을 기준으로 문자열을 나누어 배열로 저장
$arr = explode(" ", $input);

$num = $arr[0];

$game;
switch ($arr[1]) {
    case "Y":
        $game = 2;
        break;
    case "F":
        $game = 3;
        break;
    case "O":
        $game = 4;
        break;
    default:
        break;
}
$Array;

// 배열 출력 (확인용)
for ($i = 1; $i <= $num; $i++) {
    $Array[] = trim(fgets(STDIN));
}
$uniqueArray = array_unique($Array);

echo intdiv(count($uniqueArray),$game-1);
?>