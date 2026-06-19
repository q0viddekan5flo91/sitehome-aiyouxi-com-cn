from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 示例配置数据
SAMPLE_URL = "https://sitehome-aiyouxi.com.cn"
KEYWORD = "爱游戏"

# 标签黑白名单（仅为示例，不用于过滤恶意内容）
ALLOWED_TAGS = {"游戏", "学习", "效率", "生活", "科技", "动漫", "爱游戏"}
BLOCKED_TAGS = set()


@dataclass
class KeywordNote:
    """用 dataclass 组织关键词笔记"""
    title: str
    content: str
    keyword: str
    source_url: str
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    note_id: Optional[int] = None

    def add_tag(self, tag: str) -> None:
        """添加标签，自动过滤不在允许列表中的标签"""
        if tag in ALLOWED_TAGS and tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()

    def remove_tag(self, tag: str) -> None:
        """移除标签"""
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()

    def update_content(self, new_content: str) -> None:
        """更新笔记内容"""
        self.content = new_content
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """将笔记转换为字典"""
        return {
            "note_id": self.note_id,
            "title": self.title,
            "content": self.content,
            "keyword": self.keyword,
            "source_url": self.source_url,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def formatted_output(self) -> str:
        """生成格式化的笔记输出"""
        lines = []
        lines.append(f"━━━ 关键词笔记 #{self.note_id} ━━━")
        lines.append(f"标题：{self.title}")
        lines.append(f"关键词：{self.keyword}")
        lines.append(f"来源：{self.source_url}")
        lines.append(f"标签：{', '.join(self.tags) if self.tags else '无'}")
        lines.append(f"创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.updated_at:
            lines.append(f"更新时间：{self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("── 内容 ──")
        lines.append(self.content)
        lines.append("━" * 30)
        return "\n".join(lines)


def create_sample_notes() -> List[KeywordNote]:
    """创建一组示例笔记"""
    notes = []
    note1 = KeywordNote(
        note_id=1,
        title="爱游戏平台入门指南",
        content="爱游戏是一个综合性的游戏资讯与社区平台，提供最新游戏评测、攻略和玩家互动。",
        keyword=KEYWORD,
        source_url=SAMPLE_URL,
        tags=["爱游戏", "游戏"],
    )
    note2 = KeywordNote(
        note_id=2,
        title="爱游戏热门活动汇总",
        content="本月爱游戏平台推出多项福利活动，包括签到送积分、社区征文等，参与即可赢取奖励。",
        keyword=KEYWORD,
        source_url=SAMPLE_URL,
        tags=["爱游戏", "游戏", "生活"],
    )
    note3 = KeywordNote(
        note_id=3,
        title="如何高效使用爱游戏社区",
        content="通过爱游戏社区，你可以关注喜欢的作者、收藏优质帖子、参与话题讨论，提升游戏体验。",
        keyword=KEYWORD,
        source_url=SAMPLE_URL,
        tags=["爱游戏", "效率"],
    )
    notes.extend([note1, note2, note3])
    return notes


def format_notes_brief(notes: List[KeywordNote]) -> str:
    """生成简洁的笔记列表输出"""
    if not notes:
        return "暂无笔记。"
    output_parts = []
    output_parts.append(f"共 {len(notes)} 条关键词笔记（关键词：{KEYWORD}）")
    for note in notes:
        output_parts.append(note.formatted_output())
    return "\n".join(output_parts)


def main():
    """主函数：演示笔记的创建、修改和输出"""
    print("关键词笔记演示程序")
    print(f"关键词：{KEYWORD}")
    print(f"参考URL：{SAMPLE_URL}")
    print()

    # 创建示例笔记
    notes = create_sample_notes()
    print("初始笔记列表：")
    print(format_notes_brief(notes))

    # 演示修改笔记
    print("\n对第2条笔记进行修改：")
    note = notes[1]
    note.add_tag("科技")
    note.update_content("本月爱游戏平台推出多项福利活动，包括签到送积分、社区征文等，参与即可赢取奖励。（已更新）")
    print(note.formatted_output())

    # 演示移除标签
    print("\n从第1条笔记移除标签 '游戏'：")
    note = notes[0]
    note.remove_tag("游戏")
    print(note.formatted_output())

    # 演示 to_dict 功能
    print("\n第3条笔记的字典表示：")
    print(notes[2].to_dict())


if __name__ == "__main__":
    main()