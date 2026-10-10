import type { GalleryConfig } from "@/types/galleryConfig";

// 相册配置
export const galleryConfig: GalleryConfig = {
	// 相册列表
	// 添加方法：在数组中加一项（id/name/description/location/date/tags），
	// 并在 public/gallery/{id}/ 目录下放入图片（cover.* 或第一张图作为封面）。
	// 支持可选字段 password / passwordHint 设置加密相册。
	albums: [],

	// 瀑布流最小列宽(px)，浏览器根据容器宽度自动计算列数，默认 240
	// 值越小列数越多，值越大列数越少
	columnWidth: 240,
};
