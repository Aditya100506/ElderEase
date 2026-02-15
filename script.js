const heartRate = document.getElementById("heartRate");
const bp = document.getElementById("bp");
const temp = document.getElementById("temp");
const fallStatus = document.getElementById("fallStatus");
const modal = document.getElementById("modal");

const ctx = document.getElementById("vitalsChart").getContext("2d");

let chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: "Heart Rate",
            data: [],
            borderColor: "#3b82f6",
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

async function fetchLatest() {
    const res = await fetch("/latest");
    const data = await res.json();

    if (!data.heart_rate) return;

    heartRate.innerText = data.heart_rate + " bpm";
    bp.innerText = data.bp;
    temp.innerText = data.temperature + " °C";

    if (data.fall_detected) {
        fallStatus.innerText = "FALL DETECTED 🚨";
        fallStatus.style.color = "red";
    } else {
        fallStatus.innerText = "Normal";
        fallStatus.style.color = "lightgreen";
    }

    chart.data.labels.push(data.timestamp);
    chart.data.datasets[0].data.push(data.heart_rate);

    if (chart.data.labels.length > 15) {
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }

    chart.update();
}

setInterval(fetchLatest, 3000);

function triggerSOS() {
    fetch("/sos", { method: "POST" })
    .then(res => res.json())
    .then(() => {
        modal.classList.remove("hidden");
    });
}

function closeModal() {
    modal.classList.add("hidden");
}