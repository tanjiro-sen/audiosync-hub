import { useState } from "react"; import { Button } from "@/components/ui/button"; import { Input } from "@/components/ui/input"; import { Card, CardContent } from "@/components/ui/card";

export default function AudioSyncControl() { const [audioFile, setAudioFile] = useState(null); const [devices, setDevices] = useState(""); const [delay, setDelay] = useState(3);

const handleFileChange = (e) => { setAudioFile(e.target.files[0]); };

const handleStartSync = async () => { const formData = new FormData(); formData.append("audio", audioFile); formData.append("devices", devices); formData.append("delay", delay);

await fetch("http://localhost:5000/sync", {
  method: "POST",
  body: formData,
});

};

return ( <div className="p-4 grid gap-4 max-w-xl mx-auto"> <Card> <CardContent className="p-4 space-y-4"> <h2 className="text-xl font-semibold">Audio Sync Controller</h2>

<Input type="file" accept="audio/*" onChange={handleFileChange} />

      <Input
        type="text"
        placeholder="Device IPs (comma-separated)"
        value={devices}
        onChange={(e) => setDevices(e.target.value)}
      />

      <Input
        type="number"
        placeholder="Delay in seconds"
        value={delay}
        onChange={(e) => setDelay(e.target.value)}
      />

      <Button onClick={handleStartSync} disabled={!audioFile || !devices}>
        Start Playback Sync
      </Button>
    </CardContent>
  </Card>
</div>

); }

