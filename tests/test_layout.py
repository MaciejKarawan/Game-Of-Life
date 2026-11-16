from pathlib import Path
import ast, importlib, unittest
ROOT = Path(__file__).resolve().parents[1]
class LayoutChecks(unittest.TestCase):
    def test_python_compiles(self):
        for directory in ['src','scripts']:
            for f in (ROOT/directory).rglob('*.py'):compile(f.read_text(encoding='utf-8-sig'),str(f),'exec')
    def test_input_and_report_content_preserved(self):
        import json,hashlib
        rows=json.loads((ROOT/'docs/file-migration.json').read_text(encoding='utf-8'))
        for row in rows:
            if Path(row['old']).suffix.lower() not in ['.csv','.xlsx','.pdf','.png','.html']:continue
            if '.ipynb_checkpoints/' in row['old']:continue
            self.assertTrue(row['identical_content_at'],row['old'])
            self.assertTrue(any(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==row['sha256'] for f in row['identical_content_at']),row['old'])
    def test_blinker(self):
        from game_of_life.space import Space
        from game_of_life.engine import GameMaster
        s=Space(5,5);points={(2,1),(2,2),(2,3)}
        for x,y in points:s.grid[x][y].change_state()
        gm=GameMaster(s,[2,3],[3]);gm.change_space_state()
        self.assertEqual({(x,y) for x in range(5) for y in range(5) if s.grid[x][y].alive},{(1,2),(2,2),(3,2)})
        gm.change_space_state()
        self.assertEqual({(x,y) for x in range(5) for y in range(5) if s.grid[x][y].alive},points)

if __name__ == '__main__':unittest.main()
