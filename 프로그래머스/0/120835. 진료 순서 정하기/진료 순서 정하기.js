function solution(emergency) {
    let sortEmergency = emergency.slice().sort((a,b) => b - a);
    return emergency.map(v => sortEmergency.indexOf(v)+1);
}