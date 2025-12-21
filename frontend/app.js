async function main() {
  const meta = document.getElementById("meta");
  const list = document.getElementById("list");

  const res = await fetch("./data.json", { cache: "no-store" });
  if (!res.ok) {
    meta.textContent = `data.json が取得できなかった: ${res.status}`;
    return;
  }

  const data = await res.json();
  meta.textContent = `records: ${data.length}`;

  list.innerHTML = "";
  for (const row of data) {
    const li = document.createElement("li");
    li.textContent = `${row.date}: ${row.value}`;
    list.appendChild(li);
  }
}

main().catch((e) => {
  const meta = document.getElementById("meta");
  meta.textContent = `error: ${String(e)}`;
});

