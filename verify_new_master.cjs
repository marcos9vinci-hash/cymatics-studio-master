const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const ARTIFACTS_DIR = "C:/Users/Pc/.gemini/antigravity/brain/10daf2f6-2ac2-422c-ad99-627ecc795bf0";

async function runTest() {
  console.log("=== INICIANDO TESTE E VERIFICAÇÃO AUTOMATIZADA: CYMATICS STUDIO MASTER ===");

  const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
  const profileDir = path.join(__dirname, ".chrome_test_profile");

  if (!fs.existsSync(profileDir)) {
    fs.mkdirSync(profileDir, { recursive: true });
  }

  const chromeProc = spawn(chromePath, [
    "--headless=new",
    "--remote-debugging-port=9222",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    `--user-data-dir=${profileDir}`,
    "about:blank"
  ]);

  let versionData = null;
  for (let i = 0; i < 30; i++) {
    try {
      const res = await fetch("http://127.0.0.1:9222/json/version");
      versionData = await res.json();
      if (versionData) break;
    } catch (e) {
      await new Promise(r => setTimeout(r, 200));
    }
  }

  if (!versionData) {
    console.error("Chrome não respondeu!");
    chromeProc.kill();
    process.exit(1);
  }

  console.log("Conectado ao Chrome:", versionData.Browser);

  const fileUrl = "http://localhost:8080/index.html";
  const newTabRes = await fetch(`http://127.0.0.1:9222/json/new?${encodeURIComponent(fileUrl)}`, { method: 'PUT' });
  const tabData = await newTabRes.json();
  const ws = new WebSocket(tabData.webSocketDebuggerUrl);

  const consoleLogs = [];
  const pageErrors = [];
  let msgId = 1;
  const pendingRequests = new Map();

  function sendCommand(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = msgId++;
      pendingRequests.set(id, { resolve, reject });
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (data.id && pendingRequests.has(data.id)) {
      const { resolve } = pendingRequests.get(data.id);
      pendingRequests.delete(data.id);
      resolve(data.result);
    }
    if (data.method === "Runtime.consoleAPICalled") {
      const text = data.params.args.map(a => a.value || JSON.stringify(a)).join(' ');
      consoleLogs.push(`[CONSOLE ${data.params.type}] ${text}`);
      if (data.params.type === 'error') {
        pageErrors.push(text);
      }
    }
    if (data.method === "Runtime.exceptionThrown") {
      const desc = data.params.exceptionDetails.exception ? data.params.exceptionDetails.exception.description : data.params.exceptionDetails.text;
      pageErrors.push(`[EXCEPTION] ${desc}`);
    }
  };

  await new Promise(r => ws.onopen = r);

  await sendCommand('Runtime.enable');
  await sendCommand('Page.enable');
  await sendCommand('DOM.enable');
  await sendCommand("Emulation.setDeviceMetricsOverride", {
    width: 1920,
    height: 1080,
    deviceScaleFactor: 1,
    mobile: false
  });

  console.log("Aguardando carregamento da página...");
  await new Promise(r => setTimeout(r, 3000));

  async function takeScreenshot(filename) {
    const res = await sendCommand('Page.captureScreenshot', { format: 'png' });
    const buf = Buffer.from(res.data, 'base64');
    const outPath = path.join(ARTIFACTS_DIR, filename);
    fs.writeFileSync(outPath, buf);
    console.log(`📸 Screenshot salvo: ${outPath} (${buf.length} bytes)`);
    return outPath;
  }

  // 1. Estado Inicial (Silêncio, Água Plana, Ponto Central Único)
  await takeScreenshot('screen_master_silencio_puro.png');

  // 2. Ativação de Preset Solfeggio 528 Hz
  console.log("Ativando Preset 528 Hz...");
  await sendCommand('Runtime.evaluate', {
    expression: `(function() {
      const btns = Array.from(document.querySelectorAll('.preset-btn'));
      const btn528 = btns.find(b => b.innerText.includes('528'));
      if (btn528) btn528.click();
    })()`
  });

  await new Promise(r => setTimeout(r, 2000));
  await takeScreenshot('screen_master_solfeggio_528_ativo.png');

  // 3. Mudança de Geometria Sagrada para Semente da Vida
  console.log("Mudando Matriz Sagrada para Semente da Vida...");
  await sendCommand('Runtime.evaluate', {
    expression: `(function() {
      const select = document.getElementById('sacred-matrix-select');
      select.value = 'semente_vida';
      select.dispatchEvent(new Event('change'));
    })()`
  });

  await new Promise(r => setTimeout(r, 2000));
  await takeScreenshot('screen_master_semente_vida.png');

  // 4. Abertura do Modal da Luminária 3D
  console.log("Abrindo Modal da Luminária 3D...");
  await sendCommand('Runtime.evaluate', {
    expression: `document.getElementById('nav-btn-lights').click();`
  });

  await new Promise(r => setTimeout(r, 1500));
  await takeScreenshot('screen_master_modal_luminaria.png');

  // 5. Mesa 2 - Chladni Sand com 28.000 grãos
  console.log("Alternando para Mesa 2 (Chladni Sand)...");
  await sendCommand('Runtime.evaluate', {
    expression: `(function() {
      document.getElementById('close-lights-modal').click();
      document.getElementById('nav-mesa-2').click();
    })()`
  });

  await new Promise(r => setTimeout(r, 2500));
  await takeScreenshot('screen_master_chladni_sand.png');

  // 6. Mesa 3 - Fusão Híbrida
  console.log("Alternando para Mesa 3 (Fusão Híbrida)...");
  await sendCommand('Runtime.evaluate', {
    expression: `document.getElementById('nav-mesa-3').click();`
  });

  await new Promise(r => setTimeout(r, 2500));
  await takeScreenshot('screen_master_fusao_hibrida.png');

  // 7. Botão Parar Som (Silêncio Total Imediato)
  console.log("Testando parada geral de som...");
  await sendCommand('Runtime.evaluate', {
    expression: `document.getElementById('nav-btn-stop').click();`
  });

  await new Promise(r => setTimeout(r, 1500));
  await takeScreenshot('screen_master_silencio_final.png');

  // Validação final de erros no console
  console.log("==================================================");
  console.log(`TOTAL DE ERROS NO CONSOLE: ${pageErrors.length}`);
  if (pageErrors.length > 0) {
    console.error("ERROS ENCONTRADOS:", pageErrors);
  } else {
    console.log("✅ NENHUM ERRO DE JAVASCRIPT OU CONSOLE ENCONTRADO!");
  }
  console.log("==================================================");

  ws.close();
  chromeProc.kill();
  process.exit(pageErrors.length > 0 ? 1 : 0);
}

runTest().catch(err => {
  console.error("Erro fatal no teste:", err);
  process.exit(1);
});
